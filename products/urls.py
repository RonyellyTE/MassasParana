from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import produtos_por_categoria, home
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='products'),
    path('categoria/<int:categoria_id>/', produtos_por_categoria, name='produtos_por_categoria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)