# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20161225_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='multiplechoicequestions',
            name='question_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Question'),
        ),
        migrations.AlterField(
            model_name='truefalsequestion',
            name='question_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Question'),
        ),
    ]
