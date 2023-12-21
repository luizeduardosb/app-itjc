# Generated by Django 4.2.7 on 2023-12-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0019_alter_edital_imagem_alter_empresa_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='imagem',
            field=models.ImageField(blank=True, default='default.jpg', help_text='ATENÇÃO! PARA UMA MELHOR EXPERIÊNCIA DO USUÁRIO, ADICIONE APENAS IMAGENS EM PNG', null=True, upload_to='fotosEditais'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagem',
            field=models.ImageField(blank=True, default='default.jpg', help_text='ATENÇÃO! PARA UMA MELHOR EXPERIÊNCIA DO USUÁRIO, ADICIONE APENAS IMAGENS EM PNG', null=True, upload_to='logoEmpresas'),
        ),
    ]
