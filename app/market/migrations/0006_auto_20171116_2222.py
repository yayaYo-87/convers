# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 19:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20171114_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='related_goods',
            field=models.ManyToManyField(blank=True, related_name='_goods_related_goods_+', to='market.Goods', verbose_name='Похожие товары'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='accessibility',
            field=models.TextField(blank=True, null=True, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='audience',
            field=models.TextField(blank=True, null=True, verbose_name='Аудитория'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='author',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goods_categories', to='market.Category', verbose_name='Категория товаров'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='count_pages',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='date_publication',
            field=models.PositiveIntegerField(blank=True, help_text='Введите год публикации книги <YYYY>', null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2017)], verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='easy_to_use',
            field=models.TextField(blank=True, null=True, verbose_name='Простота использования'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='format',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Формат'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Короткое описание'),
        ),
    ]
