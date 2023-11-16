from django.db import models

class Email(models.Model):

    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return self.nome
