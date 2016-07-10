# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-02 14:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowboard', '0003_auto_20160531_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_id',
        ),
        migrations.AddField(
            model_name='video',
            name='video_upload',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 2, 14, 56, 10, 862246)),
        ),
    ]
