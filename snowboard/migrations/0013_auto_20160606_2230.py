# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 22:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowboard', '0012_auto_20160606_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 6, 22, 30, 46, 779485)),
        ),
    ]
