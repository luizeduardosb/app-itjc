from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from decouple import config

def enviarEmail(request):
    subject = 'Teste automatização email'
    content = 'Teste automatização email da itjc usando django'
    send_mail(subject, content, config('EMAIL_HOST_USER'), ['mariasilvasouza268@gmail.com'])
    return render(request, 'aplicacoes/home.html')
