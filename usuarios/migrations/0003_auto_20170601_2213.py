# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20170601_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(default='teste', max_length=300, verbose_name='Endereco'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
