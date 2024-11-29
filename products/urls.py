from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import products




urlpatterns = [
    path('', products, name='produtos'),
]