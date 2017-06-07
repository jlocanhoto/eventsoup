# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 17:51
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usuarios.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('telefone', models.CharField(max_length=30, verbose_name='Telefone')),
                ('cpf_cnpj', models.CharField(max_length=30, unique=True, verbose_name='CPF/CNPJ')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Cadastro')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome', unique_with=('date_joined',), verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', usuarios.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contratante',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contratante',
                'verbose_name_plural': 'Contratantes',
            },
            bases=('usuarios.usuario',),
        ),
        migrations.CreateModel(
            name='Entregador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.CharField(choices=[('Moto', 'Moto'), ('Carro', 'Carro'), ('Van', 'Van'), ('Caminhao', 'Caminhão')], max_length=50, verbose_name='Veiculo')),
            ],
            options={
                'verbose_name': 'Entregador',
                'verbose_name_plural': 'Entregadores',
            },
            bases=('usuarios.usuario',),
        ),
        migrations.CreateModel(
            name='FornecedorBuffet',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('faz_entrega', models.BooleanField(verbose_name='Faz entrega')),
            ],
            options={
                'verbose_name': 'Fornecedor (Buffet)',
                'verbose_name_plural': 'Fornecedores (Buffet)',
            },
            bases=('usuarios.usuario',),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]