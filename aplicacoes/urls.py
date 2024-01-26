from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='index'),
    path('', views.editais, name='editais'),
    path('edital/<int:id>', views.editalView, name='edital-view'),
    path('empresas', views.empresas, name='empresas'),
    path('empresa/<int:id>', views.empresaView, name='empresa-view'),
    path('', views.enviaEmail, name='email-automatico'),
]