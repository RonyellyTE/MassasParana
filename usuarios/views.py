import logging
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from django.shortcuts import render

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
        password = form.cleaned_data['senha']

        # Apenas imprime os dados no console
        print(f"Login - Email: {email}, Senha: {password}")
        logger.info(f"Tentativa de login - Email: {email}, Senha: {password}")

        # Exibe uma mensagem de sucesso
        messages.success(self.request, 'Login submetido! (Veja o terminal para os dados)')

        return super().form_valid(form)

class RegisterView(FormView):
    template_name = 'cadastro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o registro

    def form_valid(self, form):
        print("Formulário de cadastro validado com sucesso")
        logger.info("Formulário de cadastro validado com sucesso")

        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']

        # Imprime os dados no console
        print(f"Registro - Nome: {nome}, Email: {email}, Senha: {senha}")
        logger.info(f"Tentativa de registro - Nome: {nome}, Email: {email}, Senha: {senha}")

        # Exibe uma mensagem de sucesso
        messages.success(self.request, 'Cadastro realizado com sucesso! Agora você pode fazer login.')

        return super().form_valid(form)

    def form_invalid(self, form):
        print(f"Formulário inválido com erros: {form.errors}")
        logger.error(f"Formulário inválido no cadastro: {form.errors}")
        return super().form_invalid(form)

class PasswordResetView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name, context={})

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html', context={})
