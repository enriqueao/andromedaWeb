# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andromeda', '0004_auto_20170515_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='andromedadevices',
            name='creado',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]