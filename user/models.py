from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import RegexValidator


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    genero = models.CharField(
        max_length=20,
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')],
        default='Não informado'
    )
    cpf = models.CharField(
        max_length=14,  # 999.999.999-99
        validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

    def set_password(self, raw_password):
        """Define e armazena a senha hash."""
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica se a senha está correta."""
        return check_password(raw_password, self.senha)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.BinaryField()
    google_auth = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Papel(models.Model):
    usuario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    gerente = models.BooleanField(default=False)
    caixa = models.BooleanField(default=False)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.descricao}"
