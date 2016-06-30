# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import fleetboss.models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetboss', '0004_auto_20160630_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleetaccess',
            name='secret',
            field=models.CharField(db_index=True, default=fleetboss.models.get_key, max_length=24),
        ),
    ]
