# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171201_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_delivery',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Cумма заказа и доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Cумма заказа'),
        ),
    ]