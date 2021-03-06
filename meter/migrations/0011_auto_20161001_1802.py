# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('meter', '0010_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cost_kw_per_hour', models.FloatField(default=None, null=True)),
                ('send_email', models.BooleanField(default=False)),
            ],
        ),
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
