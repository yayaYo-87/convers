# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20171114_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название размера')),
            ],
            options={
                'verbose_name': 'Размер одежды',
                'verbose_name_plural': 'Размеры одежды',
            },
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['sort_index'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='goods',
            name='size',
        ),
        migrations.AddField(
            model_name='goods',
            name='size',
            field=models.ManyToManyField(blank=True, to='market.Size', verbose_name='Доступные размеры'),
        ),
    ]
