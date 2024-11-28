from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Alterado para CharField
    google_auth = models.BooleanField(default=False)

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
