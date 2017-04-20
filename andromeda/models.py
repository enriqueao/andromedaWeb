from django.db import models
from django.contrib import admin
# Create your models here.

class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nikname = models.CharField(max_length=20)
    # imagen = models.ImageField(upload_to='photos')

    def __str__(self):
        return '{} {} {}'.format(self.nombre,self.password,self.nikname)

class usuarioAdmin(admin.ModelAdmin):
    list_display = 'nombre','nikname'
