# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 20:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 31, 20, 51, 27, 812208)),
        ),
    ]
