from django.shortcuts import render, get_object_or_404
from .models import Edital
from .models import Empresa

def home(request):
    editais = Edital.objects.all()
    empresas = Empresa.objects.all()
    return render(request, 'aplicacoes/home.html', {'editais': editais, 'empresas': empresas})

def editais(request):
    editais = Edital.objects.all()
    return render(request, 'aplicacoes/home.html', {'editais': editais})

def editalView(request, id):
    edital = get_object_or_404(Edital, pk=id)
    return render(request, 'aplicacoes/edital.html', {'edital': edital})

def empresas(request):
    empresas = Empresa.objects.all()
    print(empresas)
    return render(request, 'aplicacoes/empresas.html', {'empresas': empresas})

def empresaView(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    return render(request, 'aplicacoes/empresa.html', {'empresa': empresa})


    