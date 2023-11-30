from django.shortcuts import render, get_object_or_404
from .models import Edital
from .models import Empresa
from .forms import salvar
from django.core.mail import send_mail
from decouple import config

def home(request):
    editais = Edital.objects.all()
    empresas = Empresa.objects.all()

    if request.method == 'POST':
        form = salvar(request.POST)
        if form.is_valid():
            form.save()
            
            enviaEmail(request)
            form = salvar()
    else:
        form = salvar()

    return render(request, 'aplicacoes/home.html', {'editais': editais, 'empresas': empresas, 'form' : form})

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

def enviaEmail(request):
    subject = 'Teste automatização email'
    content = 'Teste automatização email da itjc usando django'
    send_mail(subject, content, config('EMAIL_HOST_USER'), ['mariasilvasouza268@gmail.com'])
    return render(request, 'aplicacoes/home.html')
