from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        redirect_url = reverse_lazy('home')
        return redirect(redirect_url)

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', context={})

def contact(request):
    return HttpResponse("contato")

class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us.html', context={})