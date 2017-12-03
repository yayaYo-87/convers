# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20171201_0056'),
        ('mainpage', '0004_leftblog_pages'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeftAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Описание')),
                ('pages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_page', to='pages.Page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.RemoveField(
            model_name='leftblog',
            name='pages',
        ),
    ]
