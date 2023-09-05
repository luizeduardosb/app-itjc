from django.shortcuts import render, get_object_or_404
from .models import Edital
from .models import Empresa

def home(request):
    editais = Edital.objects.all()
    return render(request, 'aplicacoes/home.html', {'editais': editais})


def editalView(request, id):
    edital = get_object_or_404(Edital, pk=id)
    return render(request, 'aplicacoes/edital.html', {'edital': edital})
    