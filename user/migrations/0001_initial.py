# Generated by Django 5.1.2 on 2024-11-28 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.BinaryField()),
                ('google_auth', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.BinaryField()),
                ('google_auth', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Papel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerente', models.BooleanField(default=False)),
                ('caixa', models.BooleanField(default=False)),
                ('descricao', models.CharField(blank=True, max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.funcionario')),
            ],
        ),
    ]
