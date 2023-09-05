from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.editais, name='editais'),
    path('edital/<int:id>', views.editalView, name='edital-view'),
    path('', views.empresas, name='empresas'),
]