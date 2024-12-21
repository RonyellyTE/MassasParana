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
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.check_password(senha):
                self.request.session['cliente_id'] = cliente.id
                self.request.session['user_name'] = cliente.nome
                self.request.session['user_email'] = cliente.email
                logger.info("Cliente logged in: %s", email)
                return redirect(self.success_url)
            else:
                logger.warning("Invalid password for email: %s", email)
                messages.error(self.request, "Email ou senha incorretos.")
        except Cliente.DoesNotExist:
            logger.warning("Login attempted for non-existent email: %s", email)
            messages.error(self.request, "Usuário não encontrado.")

        return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro no login. Verifique as informações.")
        return super().form_invalid(form)


class RegisterView(FormView):
    template_name = 'cadastro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']

        try:
            usuario = Cliente.objects.create(
                nome=nome,
                email=email
            )
            usuario.set_password(senha)  # Hash and save the password securely
            usuario.save()
            messages.success(self.request, "Cadastro realizado com sucesso! Agora você pode fazer login.")
            return super().form_valid(form)

        except IntegrityError:
            logger.error("IntegrityError: Email already in use: %s", email)
            messages.error(self.request, "Erro ao realizar o cadastro. Tente novamente mais tarde.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        logger.error(f"Register form invalid: {form.errors}")
        messages.error(self.request, "Erro no formulário. Verifique as informações.")
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
    template_name = "profile.html"  # Mesma página onde será exibido o formulário
    success_url = reverse_lazy("profile")  # Redirecionamento corrigido

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
