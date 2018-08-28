# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-06 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_directoradmitbriefing_directoradmitcommunity_directoradmitparentsadmit_directoradmityear'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorAdmitParentletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField()),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('link_text', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'db_table': 'director_admit_parentletter',
                'managed': False,
            },
        ),
    ]