# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POPapp', '0011_auto_20170102_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connection',
            name='image',
        ),
        migrations.AddField(
            model_name='connection',
            name='code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]