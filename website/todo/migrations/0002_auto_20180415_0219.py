# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 09:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='createdAt',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 4, 15, 2, 19, 53, 338000)),
        ),
    ]
