# carrinho/models.py

from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from products.models import Produto 
from django.conf import settings # Importa o modelo de Produto

class Carrinho(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário personalizado
        on_delete=models.CASCADE,
        related_name='carrinho',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    def __str__(self):
        return f"Carrinho de {self.user.username if self.user else 'Visitante'}"

    def get_total(self):
        total = Decimal(0.00)
        for item in self.itens.all():
            total += item.get_subtotal()
        return total

    def get_total_items(self):
        return sum(item.quantidade for item in self.itens.all())

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto")
    quantidade = models.PositiveIntegerField(default=1, verbose_name="Quantidade")

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

    def get_subtotal(self):
        return self.produto.preco * self.quantidade
