# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0021_auto_20170629_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='restricoes',
        ),
    ]
