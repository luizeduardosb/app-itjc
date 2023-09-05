from django.db import models

class Edital(models.Model):

    STATUS = (('aberto', 'Aberto'), ('encerrado', 'Encerrado'),)

    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=250)
    materia = models.TextField()
    status = models.CharField(max_length=9, choices=STATUS,)

    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Empresa(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=200)
    site = models.CharField(max_length=100)
    contato = models.TextField()
