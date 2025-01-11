# shopping_cart/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('diminuir/<int:produto_id>/', views.diminuir_quantidade, name='diminuir_quantidade'), 
    path('aumentar_quantidade/<int:produto_id>/', views.aumentar_quantidade, name='aumentar_quantidade'), # Nova URL
    path('', views.shopping_cart_details, name='shopping_cart_details'),
]