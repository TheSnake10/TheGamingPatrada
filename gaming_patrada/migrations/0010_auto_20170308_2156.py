# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming_patrada', '0009_auto_20170308_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='release',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]