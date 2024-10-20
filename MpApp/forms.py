from django import forms

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
