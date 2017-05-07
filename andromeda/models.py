from django.db import models
from django.contrib import admin
# Create your models here.

class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return '{} {} {}'.format(self.nombre,self.password)

class andromedadevices(models.Model):
    pass

class recordatorios(models.Model):
    idRecordatorio = models.AutoField(primary_key=True)

class tiporecordatorio(models.Model):
    idTipoRecordatorio = models.AutoField(primary_key=True)
    prioridad = models.CharField(max_length=20)
# class usuarioAdmin(admin.ModelAdmin):
#     list_display = 'nombre','nikname'
