# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20161129_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u7fa4\u7ec4\u540d\u79f0'),
        ),
    ]
