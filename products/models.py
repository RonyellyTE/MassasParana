from django.db import models
from django.utils import timezone  # Importe a função timezone
from decimal import Decimal
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='categorias/', blank=True, null=True)  # Adicionado o campo de imagem
    descricao = models.TextField(verbose_name="Descrição da Categoria", blank=True)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Título do Produto")
    descricao = models.TextField(verbose_name="Descrição", default="")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    imagem = models.ImageField(upload_to='products/', verbose_name="Imagem do Produto")
    alergenicos = models.TextField(verbose_name="Alérgenos", default="")
    ingredientes = models.TextField(verbose_name="Ingredientes", default="")
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.CASCADE, related_name='produtos', verbose_name="Categoria"
    )
    quantidade = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Estoque")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.nome

    def get_alergenicos_list(self):
        return [al.strip() for al in self.alergenicos.split(';') if al.strip()]

    def get_ingredientes_list(self):
        return [ing.strip() for ing in self.ingredientes.split(';') if ing.strip()]

