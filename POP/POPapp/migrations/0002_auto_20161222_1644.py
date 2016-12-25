# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 16:44
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('POPapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
