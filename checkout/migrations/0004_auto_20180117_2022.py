# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 22:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180116_2107'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0003_auto_20180116_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Concluída'), (2, 'Cancelada')], default=0, verbose_name='Situação')),
                ('payment_option', models.CharField(choices=[('deposito', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], default='deposito', max_length=20, verbose_name='Opção de Pagamento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.Order', verbose_name='Pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos pedidos',
            },
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
    ]
