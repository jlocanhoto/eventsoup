# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 01:00
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0008_pacote_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='nome', unique=True, verbose_name='Slug'),
        ),
    ]
