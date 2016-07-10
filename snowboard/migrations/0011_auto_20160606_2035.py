# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 20:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowboard', '0010_auto_20160606_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_upload',
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 6, 20, 35, 28, 522722)),
        ),
    ]