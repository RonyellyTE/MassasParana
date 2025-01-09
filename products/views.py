from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria

def home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'products_home.html', {'categorias': categorias, 'produtos': produtos})

def produtos_por_categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    # Produtos filtrados pela categoria selecionada
    produtos_filtrados = categoria.produtos.all()
    
    # Produtos de outras categorias
    produtos_restantes = Produto.objects.exclude(categoria=categoria)
    
    # Combinar os dois conjuntos, mantendo os filtrados no topo
    produtos = list(produtos_filtrados) + list(produtos_restantes)
    
    return render(request, 'products_home.html', {
        'categorias': categorias,
        'produtos': produtos,
        'categoria_selecionada': categoria,
    })


