# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_auto_20161122_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='modified',
        ),
    ]
