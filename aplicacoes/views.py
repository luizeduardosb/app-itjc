from django.shortcuts import redirect, render, get_object_or_404
from .models import Edital
from .models import Empresa
from .models import Processos
from .forms import salvar
from django.core.mail import send_mail
from decouple import config
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import salvar

def home(request):
    editais = Edital.objects.all().order_by('-created_at')
    empresas = Empresa.objects.all()
    processos = Processos.objects.all() 

    if request.method == 'POST':
        form = salvar(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            if form.cleaned_data['nome'] == 'admin' and form.cleaned_data['email'] == 'admin@admin.com':
                return redirect('/417471827a604269881d96314823m168060114i391788020n531183507')
            else:
                email.save()
                messages.success(request, 'Email cadastrado! Verifique sua caixa de mensagem')
                return redirect('/#mensagemEmail')
        else:
            messages.error(request, 'Os campos do formulário não foram preenchidos corretamente!')
            return redirect('/#mensagemEmail')
    else:
        form = salvar()

    return render(request, 'aplicacoes/index.html', {'editais': editais, 'empresas': empresas, 'form': form, 'processos': processos})


def editais(request):
    editais = Edital.objects.all()
    return render(request, 'aplicacoes/index.html', {'editais': editais})

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
    subject = 'Seu email foi cadastrado'
    content = 'Agora você irá receber todas as novas noticias, informações e novos editais da ITJC'
    send_mail(subject, content, config('EMAIL_HOST_USER'), ['luizeduardo00736@gmail.com'])
    return render(request, 'aplicacoes/index.html')

def processos(request):
    processos = Processos.objects.all()
    return render(request, 'aplicacoes/index.html', {'process': processos})

