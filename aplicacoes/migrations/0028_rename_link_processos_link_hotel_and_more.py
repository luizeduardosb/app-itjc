# Generated by Django 4.2.7 on 2024-03-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0027_rename_procesos_processos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processos',
            old_name='link',
            new_name='link_hotel',
        ),
        migrations.RemoveField(
            model_name='processos',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='processos',
            name='nome',
        ),
        migrations.AddField(
            model_name='processos',
            name='link_incubacao',
            field=models.TextField(null=True),
        ),
    ]
