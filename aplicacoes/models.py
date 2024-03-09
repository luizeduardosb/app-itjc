from django.db import models

class Edital(models.Model):

    STATUS = (('em aberto', 'Em aberto'), ('encerrado', 'Encerrado'))
    DESTAQUE = (('sim', 'sim'), ('nao', 'nao'))

    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=250)
    materia = models.TextField()
    link = models.TextField(null=True)
    inscricao = models.TextField(null=True)
    status = models.CharField(max_length=9, choices=STATUS,)
    destaque = models.CharField(max_length=3, choices=DESTAQUE, blank=True, help_text="Caso deseja que ESSE EDITAL fique em destaque na página inicial, edite e DESMARQUE O EDITAL ANTERIOR, para não ocorrer conflito!")
    imagem = models.ImageField(upload_to='fotosEditais', null=True, blank=True, default='default.jpg')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Editais'

class Empresa(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=200, null=True, blank=True)
    endereco_digital = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    whatsapp = models.CharField(max_length=50, null=True, blank=True)
    imagem = models.ImageField(upload_to='logoEmpresas', null=True, blank=True, default='default.jpg', help_text="ATENÇÃO! PARA UMA MELHOR EXPERIÊNCIA DO USUÁRIO, ADICIONE APENAS IMAGENS EM PNG")

    def __str__(self):
        return self.nome

class Email(models.Model):
    nome = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    

class Processos(models.Model):
    nome = models.CharField(max_length=50)
    link = models.TextField(null=True)
    descricao = models.CharField(max_length=600)

    def __str__(self):
        return self.nome