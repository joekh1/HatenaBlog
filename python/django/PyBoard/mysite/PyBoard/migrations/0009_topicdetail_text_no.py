# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyBoard', '0008_auto_20160517_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicdetail',
            name='text_no',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
