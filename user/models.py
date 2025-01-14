#user.models

from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ClienteManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        cliente = self.model(email=email, **extra_fields)
        cliente.set_password(password)  # Criptografa a senha
        cliente.save(using=self._db)
        return cliente

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Cliente(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(
        max_length=20,
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')],
        default='Não informado'
    )
    cpf = models.CharField(
    max_length=14, 
    validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')],
    blank=True,
    null=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClienteManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

