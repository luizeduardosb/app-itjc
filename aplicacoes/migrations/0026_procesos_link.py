# Generated by Django 4.2.7 on 2024-03-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0025_rename_process_procesos'),
    ]

    operations = [
        migrations.AddField(
            model_name='procesos',
            name='link',
            field=models.TextField(null=True),
        ),
    ]