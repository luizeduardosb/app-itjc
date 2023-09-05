from django.shortcuts import render

def home(request):
    return render(request, 'aplicacoes/home.html')
