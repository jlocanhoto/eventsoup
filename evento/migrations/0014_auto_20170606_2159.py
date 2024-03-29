# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 00:59
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0013_auto_20170606_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='nome', unique_with=('data',), verbose_name='Slug'),
        ),
    ]
