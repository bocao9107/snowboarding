# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 20:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowboard', '0011_auto_20160606_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 6, 20, 37, 34, 466680)),
        ),
    ]
