# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0002_auto_20160929_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_kw_per_hour', models.FloatField(blank=True, default=None, null=True)),
                ('send_email', models.BooleanField(default=False)),
            ],
        ),
    ]