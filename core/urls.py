"""
Configuração de URL para projeto MassasParana.

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações consulte:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Exemplos:
Visualizações de função
    1. Adicione uma importação: das visualizações de importação my_app
    2. Adicione um URL aos urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
    1. Adicione uma importação: from other_app.views import Home
    2. Adicione um URL aos urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
    1. Importe a função include(): from django.urls import include, path
    2. Adicione um URL aos urlpatterns: path('blog/', include('blog.urls'))

Descrição: Define o mapeamento de URLs para views. É aqui que você configura quais URLs devem ser tratadas por quais funções ou classes.
"""
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('user/', include('user.urls'))
]
