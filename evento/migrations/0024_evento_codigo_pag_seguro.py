# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0023_auto_20170705_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='codigo_pag_seguro',
            field=models.CharField(default='a', max_length=45, unique=True, verbose_name='Código de transação do Pag Seguro'),
            preserve_default=False,
        ),
    ]