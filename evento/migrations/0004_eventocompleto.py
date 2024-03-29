# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 14:16
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacotes', '0002_auto_20170601_1751'),
        ('evento', '0003_auto_20170603_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoCompleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id', unique_with=('evento',), verbose_name='Slug')),
                ('contratante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to=settings.AUTH_USER_MODEL, verbose_name='Fornecedor do Pacote')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evento', to='evento.Evento', verbose_name='Evento')),
                ('pacote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacote', to='pacotes.Pacote', verbose_name='Pacote do Evento')),
            ],
            options={
                'verbose_name': 'Evento Completo',
                'verbose_name_plural': 'Eventos Completos',
            },
        ),
    ]
