# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0015_auto_20170607_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='restricoes',
            field=models.CharField(blank=True, choices=[('vegetariano', 'Vegetariano'), ('regional', 'Regional')], max_length=50, null=True, verbose_name='Tipos de Alimentos'),
        ),
    ]
