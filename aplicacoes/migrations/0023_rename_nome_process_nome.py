# Generated by Django 4.2.7 on 2024-03-03 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0022_process'),
    ]

    operations = [
        migrations.RenameField(
            model_name='process',
            old_name='Nome',
            new_name='nome',
        ),
    ]
