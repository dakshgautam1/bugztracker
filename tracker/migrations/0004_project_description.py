# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_task_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
    ]