# -*- coding:utf-8 -*_
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Count
from django.shortcuts import render,redirect
from django.template import loader,Context
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.generic import *
from django.core.urlresolvers import *
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from andromeda.models import *
from andromeda.forms import *
# Create your views here.

@login_required
def usuario(request):

    return render(request,'principal.html')

@csrf_exempt
def ayuda(request):
    return render(request, 'help.html')

@csrf_exempt
def perfil(request):
    return render(request, 'perfil.html')

@csrf_exempt
def recordatorio(request):
    return render(request, 'recordatorio.html')

@csrf_exempt
def graficar(request):
    idAndromedaUser = request.POST.get('idAndromeda',False)
    pendientes = len(list(recordatorios.objects.filter(idAndromedaUser=idAndromedaUser,idEstadoRecordatorio=1).values('idEstadoRecordatorio')))
    eliminados = len(list(recordatorios.objects.filter(idAndromedaUser=idAndromedaUser,idEstadoRecordatorio=2).values('idEstadoRecordatorio')))
    completados = len(list(recordatorios.objects.filter(idAndromedaUser=idAndromedaUser,idEstadoRecordatorio=3).values('idEstadoRecordatorio')))
    data = {}
    data['pendientes'] = pendientes
    data['eliminados'] = eliminados
    data['completados'] = completados
    return HttpResponse(json.dumps(data), content_type = "application/json")

@csrf_exempt
def recordatoriosPendientes(request):
    if request.method == 'POST':
        idAndromedaUser = request.POST.get('id',False)
        recordatorio =  serializers.serialize('json',recordatorios.objects.filter(idAndromedaUser=idAndromedaUser,idEstadoRecordatorio=1))
        return HttpResponse(recordatorio, content_type='application/json')

@csrf_exempt
def guardarRecordatorio(request):
    idTipoRecordatorio = request.POST.get('idTipoRecordatorio',False)
    iduser = request.POST.get('id')
    diaRecordatorio = request.POST.get('diaRecordatorio',False)
    descripcion = request.POST.get('descripcion',False)
    horaRecordar = request.POST.get('horaRecordar',False)
    if request.method == 'POST':
        r = recordatorios(idAndromedaUser=iduser,idTipoRecordatorio=idTipoRecordatorio,diaRecordatorio=diaRecordatorio,descripcion=descripcion,horaRecordar=horaRecordar)
        r.save()
        return HttpResponse('1')

@csrf_exempt
def eliminarRecordatorio(request):
    primary = request.POST.get('primary')
    if request.method == 'POST':
        recordatorios.objects.filter(pk=primary).update(idEstadoRecordatorio='2')
        return HttpResponse('1')

@csrf_exempt
def completarRecordatorio(request):
    primary = request.POST.get('primary')
    if request.method == 'POST':
        recordatorios.objects.filter(pk=primary).update(idEstadoRecordatorio='3')
        return HttpResponse('1')

@csrf_exempt
def andromeda(request):
    return render(request, 'andromeda.html')

@csrf_exempt
def bienvenida(request):
    if request.user.is_authenticated():
        return render(request,'principal.html')
    else:
        return render(request,'index.html')

@csrf_exempt
def registro(request):
    if request.method == 'POST':
        idAndromeda = request.POST.get('idAndromeda',False)
        username = request.POST.get('username',False)
        if(andromedadevices.objects.filter(idAndromeda=idAndromeda).exists()):
            if(not (User.objects.filter(username=username).exists())):
                first_name = request.POST.get('nombreCompleto',False)
                email = request.POST.get('correo',False)
                password = request.POST.get('password',False)
                exito = User.objects.create_user(username=username, password=password,email=email,first_name=first_name)
                usuario =  User.objects.values('id').filter(username=username)
                r = andromedaUsers(idAndromedaUser_id=usuario[0]['id'],idAndromeda_id=idAndromeda)
                r.save()
                return HttpResponse('1')
            else:
                return HttpResponse('2')
        else:
            return HttpResponse('0');

@csrf_exempt
def login_user(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password',None)
    acceso = authenticate(username=username,password=password)
    if acceso is not None and acceso.is_active:
        crearSession(request,username)
        login(request,acceso)
        respuesta = '1'
    else:
        respuesta = '0'
    return HttpResponse(respuesta);

@csrf_exempt
def crearSession(request,username):
    usuario =  User.objects.values('id','username','email').filter(username=username)
    userAndromeda =  andromedaUsers.objects.values('idAndromeda','imagen').filter(idAndromedaUser=usuario[0]['id'])
    request.session['user'] = usuario[0]
    request.session['userAndromeda'] = userAndromeda[0]
    request.session['idAndromeda'] = userAndromeda[0]['idAndromeda']
