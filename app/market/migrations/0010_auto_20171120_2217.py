# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 19:17
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20171119_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание'),
        ),
    ]