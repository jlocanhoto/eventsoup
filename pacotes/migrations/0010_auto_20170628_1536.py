# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0009_auto_20170628_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='codigo_pag_seguro',
            field=models.CharField(max_length=32, unique=True, verbose_name='Código do Pag Seguro'),
        ),
    ]
