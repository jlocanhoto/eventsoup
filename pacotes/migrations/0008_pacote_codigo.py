# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0007_auto_20170613_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacote',
            name='codigo',
            field=models.CharField(default='a', max_length=5, unique=True, verbose_name='Código do Pacote'),
            preserve_default=False,
        ),
    ]