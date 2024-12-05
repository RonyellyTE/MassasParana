from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', context={})

def contact(request):
    return HttpResponse("contato")

def about_us(request):
    return HttpResponse("sobre_nos")