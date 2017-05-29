# -*- coding:utf-8 -*_
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import datetime

class andromedadevices(models.Model):
    idAndromeda = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

class andromedaUsers(models.Model):
    idAndromedaUser = models.OneToOneField(User, primary_key=True)
    idAndromeda = models.ForeignKey(andromedadevices,null=False,blank=False,on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    estatus = models.IntegerField(default="1")
    imagen = models.CharField(max_length=50,default="users.svg");

class tiporecordatorio(models.Model):
    idTipoRecordatorio = models.AutoField(primary_key=True)
    prioridad = models.CharField(max_length=20)

class EstadosRecordatorios(models.Model):
    idEstadoRecordatorio = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

class recordatorios(models.Model):
    idRecordatorio = models.AutoField(primary_key=True)
    idAndromedaUser = models.IntegerField(default="0")
    idTipoRecordatorio = models.IntegerField(default="0")
    fechaCreado = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    diaRecordatorio = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    descripcion = models.CharField(max_length=50,null=False,default='Sin Información Disponible')
    idEstadoRecordatorio = models.IntegerField(default="1")
    horaRecordar = models.TimeField(blank=True, null=True)

# class usuarioAdmin(admin.ModelAdmin):
#     list_display = 'nombre','nikname'
