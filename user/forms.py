from django import forms
from .models import Cliente

class RegisterForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form__field',
        'placeholder': 'Nome completo'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form__field',
        'placeholder': 'Email'
    }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__field',
        'placeholder': 'Senha'
    }))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form__field',
        'placeholder': 'Email'
    }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__field',
        'placeholder': 'Senha'
    }))


class ClienteEditForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'genero', 'cpf', 'data_nascimento', 'telefone']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
