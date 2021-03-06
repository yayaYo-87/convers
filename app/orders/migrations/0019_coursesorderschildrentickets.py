# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-07 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20180325_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesOrdersChildrentickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('camp', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'courses_orders_childrentickets',
            },
        ),
        migrations.AddField(
            model_name='PracticumTickets',
            name='is_children',
            field=models.BooleanField(default=True, verbose_name='Билет для ребенка'),
        ),
    ]
