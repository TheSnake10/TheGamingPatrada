# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaming_patrada', '0016_auto_20170218_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='Date Released',
            new_name='released',
        ),
    ]
