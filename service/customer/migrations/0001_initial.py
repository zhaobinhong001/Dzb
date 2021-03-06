# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64)),
                ('is_active', models.BooleanField()),
                ('order', models.IntegerField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='customer.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories (django-mptt)',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('capital', models.BooleanField()),
                ('area', models.BigIntegerField(blank=True, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cities (django-select2)',
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(help_text=b'ISO 3166-1 alpha-2 - two character country code', max_length=2)),
                ('independence_day', models.DateField(blank=True, null=True)),
                ('area', models.BigIntegerField(blank=True, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, help_text=b'Try and enter few some more lines')),
                ('architecture', models.TextField(blank=True)),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Continent')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.SmallIntegerField(choices=[(1, b'Tall'), (2, b'Normal'), (3, b'Short')])),
                ('description', models.TextField(blank=True)),
                ('is_quiet', models.BooleanField()),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ImportExportItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quality', models.SmallIntegerField(choices=[(1, b'Awesome'), (2, b'Good'), (3, b'Normal'), (4, b'Bad')], default=1)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KitchenSink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('help_text', models.CharField(help_text=b'Enter fully qualified name', max_length=64)),
                ('multiple_in_row', models.CharField(help_text=b'Help text for multiple', max_length=64)),
                ('multiple2', models.CharField(blank=True, max_length=10)),
                ('textfield', models.TextField(blank=True, help_text=b'Try and enter few some more lines', verbose_name=b'Autosized textarea')),
                ('file', models.FileField(blank=True, upload_to=b'.')),
                ('readonly_field', models.CharField(default=b'Some value here', max_length=127)),
                ('date', models.DateField(blank=True, null=True)),
                ('date_and_time', models.DateTimeField(blank=True, null=True)),
                ('date_widget', models.DateField(blank=True, null=True)),
                ('datetime_widget', models.DateTimeField(blank=True, null=True)),
                ('boolean', models.BooleanField(default=True)),
                ('boolean_with_help', models.BooleanField(help_text=b'Boolean field with help text')),
                ('horizontal_choices', models.SmallIntegerField(choices=[(1, b'Awesome'), (2, b'Good'), (3, b'Normal'), (4, b'Bad')], default=1, help_text=b'Horizontal choices look like this')),
                ('vertical_choices', models.SmallIntegerField(choices=[(1, b'Hot'), (2, b'Normal'), (3, b'Cold')], default=2, help_text=b'Some help on vertical choices')),
                ('choices', models.SmallIntegerField(choices=[(1, b'Tall'), (2, b'Normal'), (3, b'Short')], default=3, help_text=b'Help text')),
                ('hidden_checkbox', models.BooleanField()),
                ('hidden_choice', models.SmallIntegerField(blank=True, choices=[(1, b'Tall'), (2, b'Normal'), (3, b'Short')], default=2)),
                ('hidden_charfield', models.CharField(blank=True, max_length=64)),
                ('hidden_charfield2', models.CharField(blank=True, max_length=64)),
                ('enclosed1', models.CharField(blank=True, max_length=64)),
                ('enclosed2', models.CharField(blank=True, max_length=64)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreign_key_country', to='customer.Country')),
                ('linked_foreign_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreign_key_linked', to='customer.Country')),
                ('raw_id_field', models.ForeignKey(blank=True, help_text=b'Regular raw ID field', null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Microwave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.SmallIntegerField(choices=[(1, b'Tall'), (2, b'Normal'), (3, b'Short')], default=2, help_text=b'Choose wisely')),
                ('is_compact', models.BooleanField()),
                ('order', models.PositiveIntegerField()),
                ('kitchensink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.KitchenSink')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ReversionedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quality', models.SmallIntegerField(choices=[(1, b'Awesome'), (2, b'Good'), (3, b'Normal'), (4, b'Bad')], default=1)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WysiwygEditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('redactor', models.TextField(blank=True, verbose_name=b'Redactor small')),
                ('redactor2', models.TextField(blank=True, verbose_name=b'Redactor2')),
                ('ckeditor', models.TextField(blank=True, verbose_name=b'CKEditor')),
            ],
        ),
        migrations.AddField(
            model_name='fridge',
            name='kitchensink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.KitchenSink'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Country'),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'country')]),
        ),
    ]
