# Generated by Django 4.2.5 on 2023-09-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacoes', '0004_rename_site_empresa_endereco_digital_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='imagem',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='editais/'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='status',
            field=models.CharField(choices=[('em aberto', 'Em aberto'), ('encerrado', 'Encerrado')], max_length=9),
        ),
    ]