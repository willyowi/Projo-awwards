# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-09 18:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aww', '0002_auto_20190909_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 18, 56, 42, 139149, tzinfo=utc)),
        ),
    ]