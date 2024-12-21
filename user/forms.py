from django import forms
from .models import Cliente

# Reusable widget attributes
form_field_attrs = {'class': 'form__field'}

class RegisterForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={**form_field_attrs, 'placeholder': 'Nome completo'}),
        error_messages={'required': 'Por favor, insira seu nome.'}
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={**form_field_attrs, 'placeholder': 'Email'}),
        error_messages={'required': 'Por favor, insira seu email.', 'invalid': 'Insira um email válido.'}
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={**form_field_attrs, 'placeholder': 'Senha'}),
        error_messages={'required': 'Por favor, insira sua senha.'}
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={**form_field_attrs, 'placeholder': 'Email'}),
        error_messages={'required': 'Por favor, insira seu email.', 'invalid': 'Insira um email válido.'}
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={**form_field_attrs, 'placeholder': 'Senha'}),
        error_messages={'required': 'Por favor, insira sua senha.'}
    )

class ClienteEditForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'genero', 'cpf', 'data_nascimento', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={**form_field_attrs}),
            'email': forms.EmailInput(attrs={**form_field_attrs}),
            'genero': forms.Select(attrs={**form_field_attrs}),
            'cpf': forms.TextInput(attrs={**form_field_attrs}),
            'data_nascimento': forms.DateInput(attrs={**form_field_attrs, 'type': 'date'}),
            'telefone': forms.TextInput(attrs={**form_field_attrs}),
        }
        error_messages = {
            'nome': {'required': 'Por favor, insira seu nome.'},
            'email': {'required': 'Por favor, insira seu email.', 'invalid': 'Insira um email válido.'},
        }
