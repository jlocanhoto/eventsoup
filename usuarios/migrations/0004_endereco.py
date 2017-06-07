# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 01:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20170601_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=250, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=250, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=250, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=250, verbose_name='Estado')),
                ('cep', models.CharField(max_length=250, verbose_name='CEP')),
                ('numero', models.CharField(max_length=250, verbose_name='Número')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to=settings.AUTH_USER_MODEL, verbose_name='Endereço do usuário')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
