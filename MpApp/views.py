from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        
    })

def login(request):
    print(request.POST)
    return render(request, 'login.html', context={
        
    })
