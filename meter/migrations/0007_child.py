# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0006_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='meter.Parent')),
                ('att2', models.IntegerField()),
            ],
        ),
    ]