# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20161227_0407'),
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
