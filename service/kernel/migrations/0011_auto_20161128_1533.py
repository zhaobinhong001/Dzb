# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0010_auto_20161128_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseuser',
            name='bank_num',
            field=models.IntegerField(verbose_name='\u94f6\u884c\u8d26\u53f7'),
        ),
    ]
