# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-07 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170107_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='version',
        ),
        migrations.AddField(
            model_name='quiz',
            name='version',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='text',
            name='version',
            field=models.TextField(default=1),
        ),
    ]
