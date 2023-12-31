# Generated by Django 4.2.7 on 2023-12-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0020_alter_edital_imagem_alter_empresa_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='destaque',
            field=models.CharField(blank=True, choices=[('sim', 'sim'), ('nao', 'nao')], help_text='Caso deseja que ESSE EDITAL fique em destaque na página inicial, edite e DESMARQUE O EDITAL ANTERIOR, para não ocorrer conflito!', max_length=3),
        ),
        migrations.AlterField(
            model_name='edital',
            name='imagem',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='fotosEditais'),
        ),
    ]
