# Generated by Django 4.2.5 on 2023-09-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0008_alter_edital_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='imagem',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
