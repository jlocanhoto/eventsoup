# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_endereco_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='slug',
        ),
    ]
