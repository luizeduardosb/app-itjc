# Generated by Django 4.2.7 on 2024-03-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0023_rename_nome_process_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]