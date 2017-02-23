# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming_patrada', '0019_auto_20170219_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='downloadlinks',
        ),
        migrations.RemoveField(
            model_name='games',
            name='released',
        ),
        migrations.AddField(
            model_name='games',
            name='download',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='games',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
