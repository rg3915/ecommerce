# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
            options={
                'verbose_name': 'categoria',
                'ordering': ['name'],
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='identificador')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='preço')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'produto',
                'ordering': ['name'],
                'verbose_name_plural': 'produtos',
            },
        ),
    ]
