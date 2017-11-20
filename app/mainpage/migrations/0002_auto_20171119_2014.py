# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 17:14
from __future__ import unicode_literals

import app.market.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topbanner',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='leftblog',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='topbanner',
            name='cover',
            field=models.ImageField(blank=True, upload_to=app.market.models.upload_to, verbose_name='Баннер'),
        ),
    ]
