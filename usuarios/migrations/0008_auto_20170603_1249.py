# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_remove_usuario_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(max_length=20, verbose_name='Estado'),
        ),
    ]
