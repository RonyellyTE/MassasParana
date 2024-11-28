import logging
from django.views import View
from django.views.generic import FormView
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from django.shortcuts import render
from .models import Cliente

logger = logging.getLogger(__name__)

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', context={})



class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profile')  # URL de sucesso após o login

    def form_valid(self, form):
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']

        try:
            # Busca o cliente pelo email
            cliente = Cliente.objects.get(email=email)

            # Verifica a senha
            if cliente.check_password(senha):
                # Cria a sessão do usuário
                self.request.session['user_id'] = cliente.id
                self.request.session['user_name'] = cliente.nome
                self.request.session['user_email'] = cliente.email  # Adicionando o email na sessão

                # Adiciona uma mensagem de sucesso
                messages.success(self.request, f"Bem-vindo(a), {cliente.nome}!")

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

from django.shortcuts import redirect

from django.shortcuts import render
from django.views import View

class ProfileView(View):
    def get(self, request):
        user_name = request.session.get('user_name', 'Usuário')  # Recupera o nome do usuário da sessão
        user_email = request.session.get('user_email', 'Email não encontrado')  # Recupera o email da sessão
        return render(request, 'profile.html', {'user_name': user_name, 'user_email': user_email})


class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage.html', context={})
    
class LogoutUserView(View):
    def get(self, request):
        return HttpResponse("Deslogado")