# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0018_evento_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.CharField(blank=True, max_length=400, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='orcamento',
            field=models.FloatField(verbose_name='Orçamento para o evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='pacotes',
            field=models.ManyToManyField(related_name='pacotes', to='pacotes.Pacote', verbose_name='Pacotes do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='quantidade_pessoas',
            field=models.PositiveIntegerField(verbose_name='Quantidade de pessoas'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='restricoes',
            field=models.CharField(blank=True, choices=[('vegetariano', 'Vegetariano'), ('regional', 'Regional')], max_length=50, null=True, verbose_name='Tipos de alimentos'),
        ),
    ]