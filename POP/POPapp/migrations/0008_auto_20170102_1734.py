# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POPapp', '0007_auto_20170102_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='url',
            field=models.ImageField(default='/static/pic_folder/no-image.png', upload_to='/static/pic_folder/'),
        ),
    ]
