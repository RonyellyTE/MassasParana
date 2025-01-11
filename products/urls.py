from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import (produtos_por_categoria, home, produto_detalhes)
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='products'),
    path('categoria/<int:categoria_id>/', produtos_por_categoria, name='produtos_por_categoria'),
    path('produto/<int:produto_id>/', produto_detalhes, name='produto_detalhes'),  
]