# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andromeda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recordatorios',
            fields=[
                ('idRecordatorio', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nikname',
        ),
    ]
