from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edital/<int:id>', views.editalView, name='edital-view'),
]