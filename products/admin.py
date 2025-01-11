from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'descricao')  # Exibe o nome e a imagem no admin
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'created_at')
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')
