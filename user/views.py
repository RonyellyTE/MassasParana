import logging
from django.views import View
from django.views.generic import FormView
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, ClienteEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from .models import Cliente

logger = logging.getLogger(__name__)

class IndexView(View):
    def get(self, request):
        redirect_url = reverse_lazy('profile')
        return redirect(redirect_url)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profile')  # URL do perfil do cliente

    def form_valid(self, form):
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']

        try:
            # Busca o cliente pelo email
            cliente = Cliente.objects.get(email=email)

            # Verifica a senha
            if cliente.check_password(senha):
                # Cria a sessão do cliente
                self.request.session['cliente_id'] = cliente.id
                self.request.session['user_name'] = cliente.nome
                self.request.session['user_email'] = cliente.email

                # Redireciona para o perfil
                return redirect(self.success_url)
            else:
                messages.error(self.request, "Email ou senha incorretos.")
                return self.form_invalid(form)
        except Cliente.DoesNotExist:
            messages.error(self.request, "Usuário não encontrado.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro no login. Verifique as informações e tente novamente.")
        return super().form_invalid(form)



class RegisterView(FormView):
    template_name = 'cadastro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')  # Redireciona para o login após o registro

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']

        # Verifica se o email já está registrado
        if get_user_model().objects.filter(email=email).exists():
            messages.error(self.request, "Este email já está em uso. Tente outro.")
            return self.form_invalid(form)

        try:
            # Cria o novo usuário
            usuario = Cliente.objects.create(
                nome=nome,
                email=email,
                senha=senha,  # Lembre-se de criptografar a senha, se necessário
            )
            usuario.set_password(senha)  # Criptografa a senha
            usuario.save()
            
            messages.success(self.request, "Cadastro realizado com sucesso! Agora você pode fazer login.")
            return super().form_valid(form)

        except IntegrityError as e:
            # Em caso de erro de integridade (ex: email duplicado)
            messages.error(self.request, "Erro ao tentar realizar o cadastro. Tente novamente mais tarde.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Exibe os erros no console
        print(f"Formulário inválido com erros: {form.errors}")
        logger.error(f"Formulário inválido no cadastro: {form.errors}")
        return super().form_invalid(form)


class PasswordResetView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name, context={})

class ProfileView(View):
    def get(self, request):
        # Recupera o ID do cliente autenticado
        cliente_id = request.session.get('cliente_id')
        if not cliente_id:
            messages.error(request, "Você precisa estar logado para acessar essa página.")
            return redirect('login')

        # Busca o cliente no banco de dados
        cliente = get_object_or_404(Cliente, id=cliente_id)

        context = {
            'user_name': cliente.nome,
            'cliente': cliente,
        }
        return render(request, 'profile.html', context)



class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage.html', context={})
    
class LogoutUserView(View):
    def get(self, request):
        # Limpa os dados da sessão
        request.session.flush()
        messages.success(request, "Você foi deslogado com sucesso.")
        return redirect('login')  # Redireciona para a página de login


class ProductsView(View):
    def get(self, request):
        return render(request, 'products.html', context={})

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteEditForm
    template_name = "editar_cliente.html"  # Template para a edição
    success_url = reverse_lazy("perfil_usuario")  # Redirecionamento após sucesso

    def get_object(self, queryset=None):
        """
        Sobrescreve o método get_object para garantir que o cliente que está editando seja o correto,
        com base nas informações da sessão (id do cliente).
        """
        cliente_id = self.request.session.get('cliente_id')
        if not cliente_id:
            # Se o id do cliente não estiver na sessão, redireciona para a página de login
            messages.error(self.request, "Você precisa estar logado para acessar esta página.")
            return redirect('login')  # Redireciona para o login se a sessão não for válida
        return get_object_or_404(Cliente, id=cliente_id)

    def form_valid(self, form):
        """
        Sobrescreve o método form_valid para exibir uma mensagem de sucesso.
        """
        messages.success(self.request, "Perfil atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Sobrescreve o método form_invalid para exibir uma mensagem de erro.
        """
        messages.error(self.request, "Erro ao atualizar o perfil. Verifique os dados e tente novamente.")
        return super().form_invalid(form)

