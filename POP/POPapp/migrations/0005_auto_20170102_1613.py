# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POPapp', '0004_auto_20170102_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='component_ptr',
            field=models.OneToOneField(auto_created=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='POPapp.Component'),
            preserve_default=False,
        ),
    ]
