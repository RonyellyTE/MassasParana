# Generated by Django 5.1.2 on 2025-01-10 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição da Categoria'),
        ),
    ]