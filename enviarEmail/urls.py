from django.urls import path
from . import views

urlpatterns = [
    path('', views.enviarEmail, name ='enviarEmail.urls')
]