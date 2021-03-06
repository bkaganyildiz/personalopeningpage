# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POPapp', '0005_auto_20170102_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='component_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='POPapp.Component'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='background',
            name='url',
            field=models.ImageField(default='pic_folder/no-image.png', upload_to='pic_folder/'),
        ),
    ]
