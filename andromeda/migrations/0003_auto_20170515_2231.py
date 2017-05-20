# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 03:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('andromeda', '0002_auto_20170424_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='andromedadevices',
            fields=[
                ('idAndromeda', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=50)),
                ('creado', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='andromedaUsers',
            fields=[
                ('idAndromedaUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_joined', models.DateField()),
                ('estatus', models.IntegerField()),
                ('imagen', models.CharField(max_length=50)),
                ('idAndromeda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='andromeda.andromedadevices')),
            ],
        ),
        migrations.CreateModel(
            name='EstadosRecordatorios',
            fields=[
                ('idEstadoRecordatorio', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tiporecordatorio',
            fields=[
                ('idTipoRecordatorio', models.AutoField(primary_key=True, serialize=False)),
                ('prioridad', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='descripcion',
            field=models.CharField(default='Sin Información Disponible', max_length=50),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='diaRecordatorio',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='fechaCreado',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='idAndromedaUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='andromeda.andromedaUsers'),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='idEstadoRecordatorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='andromeda.EstadosRecordatorios'),
        ),
        migrations.AddField(
            model_name='recordatorios',
            name='idTipoRecordatorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='andromeda.tiporecordatorio'),
        ),
    ]