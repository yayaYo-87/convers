# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20171205_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='send_to_shiptor',
            field=models.BooleanField(default=False, verbose_name='Отправлен в шиптор'),
        ),
    ]
