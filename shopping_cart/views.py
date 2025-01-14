# carrinho/views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Carrinho, ItemCarrinho
from products.models import Produto
from django.contrib.auth.decorators import login_required

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))  # Default para 1
        item, item_created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
        if not item_created:
            item.quantidade += quantidade
        else:
            item.quantidade = quantidade
        item.save()

    # Redireciona para a página do carrinho
    return redirect('shopping_cart_details')

@login_required
def remover_do_carrinho(request, produto_id):
    carrinho = get_object_or_404(Carrinho, user=request.user)
    item = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto_id=produto_id)

    item.delete()
    return redirect('shopping_cart_details')


@login_required
def shopping_cart_details(request):
    cart, _ = Carrinho.objects.get_or_create(user=request.user)
    return render(request, 'shopping_cart_deails_.html', {'carrinho': cart})


@login_required
def diminuir_quantidade(request, produto_id):
    carrinho = get_object_or_404(Carrinho, user=request.user)
    item = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto_id=produto_id)

    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()

    return redirect('shopping_cart_details')

# carrinho/views.py

@login_required
def aumentar_quantidade(request, produto_id):
    # Recupera o produto
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Recupera o carrinho do usuário, ou cria um se não existir
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    
    # Tenta recuperar o item do carrinho para o produto específico
    item, item_created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    
    # Se o item já existir, aumenta a quantidade
    if not item_created:
        item.quantidade += 1
        item.save()
    
    # Redireciona de volta para a página de detalhes do carrinho
    return redirect('shopping_cart_details')
