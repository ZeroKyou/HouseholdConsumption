# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0004_auto_20161001_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]