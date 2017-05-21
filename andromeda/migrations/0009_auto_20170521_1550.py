# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andromeda', '0008_auto_20170521_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordatorios',
            name='horaRecordar',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='andromedausers',
            name='imagen',
            field=models.CharField(default='user.svg', max_length=50),
        ),
        migrations.AlterField(
            model_name='recordatorios',
            name='diaRecordatorio',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recordatorios',
            name='idEstadoRecordatorio',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='andromeda.EstadosRecordatorios'),
        ),
    ]
