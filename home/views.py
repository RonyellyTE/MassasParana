from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("home")

def contact(request):
    return HttpResponse("contato")

def about_us(request):
    return HttpResponse("sobre_nos")