# -*- coding:utf-8 -*_
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
def andromeda(request):
    return render(request, 'andromeda.html')

@csrf_exempt
def bienvenida(request):
    if request.user.is_authenticated():
        return render(request,'principal.html')
    else:
        return render(request,'index.html')

def registro(request):
    if request.method == 'POST':
        idAndromeda = request.POST.get('idAndromeda',False)
        username = request.POST.get('username',False)
        if(andromedadevices.objects.filter(idAndromeda=idAndromeda).exists()):
            if(User.objects.filter(username=username).exists()):
                first_name = request.POST.get('nombreCompleto',False)
                email = request.POST.get('correo',False)
                password = request.POST.get('password',False)
                exito = User.objects.create_user(username=username, password=password,email=email,first_name=first_name)
                return HttpResponse('1')
            else:
                return HttpResponse('2')
        else:
            return HttpResponse('0');


def login_user(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password',None)
    acceso = authenticate(username=username,password=password)
    if acceso is not None:
        usuario = User.objects.filter(username=username)
        request.session['username'] = username
        login(request,acceso)
        respuesta = '1'
    else:
        respuesta = '0'
    return HttpResponse(respuesta);

# def login_view(request):
#     username = request.POST.get('username',False)
#     password = request.POST.get('password',False)
#     user = authenticate(username=username, password=password)
#     print(username,password)
#     if user is not None and user.is_active:
#         login(request, user)
#         # return HttpResponseRedirect("/n1.html")# Redirect to a success page.
#         print(1)
#     else:
#         # return HttpResponseRedirect("/account/invalid/")# Return a 'disabled account' error message
#         print(0)
#     return render(request,'enter.html')

# def index(request):
#     form = LoginForm(request.POST or None)
#     if method.request == 'POST':
#         if form.is_valid():
#             data = form.cleaned_data
#             nombres_usuarios = data.get('name_user')
#             contrasenia_usuarios = data.get('password_user')
#             acceso = authenticate(username=nombres_usuarios,password=contrasenia_usuarios)
#             if acceso is not None:
#                 login(request,acceso)
#             else:
#                 return HttpResponseRedirect('/andromeda')
#     else:
#         form = LoginForm()
#     return render(request,'login.html')

#
# def index(request):
#     user = usuario.objects.filter(idUsuario = 1)
#     mi_contexto = {'user':user}
#     return render(request,'archive.html',mi_contexto)
#
# def formUsuario(request):
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('andromeda:index')
#     else:
#         form = UsuarioForm()
#
#     return render(request,'registarUsuario.html',{'form':form})
#
# def usuarioEditar(request,idUser):
#     user = usuario.objects.get(idUsuario=idUser)
#     if request.method == 'GET':
#         form = UsuarioForm(instance=usuario)
#     else:
#         form =  UsuarioForm(request.POST,instance=usuario)
#         if form.is_valid():
#             form.save()
#         return redirect('adromeda:usuario')
#     return render(request,'registarUsuario.html',{'form':form})
#
#
# def usuarioDelete(request,idUser):
#     user = user.objects.get(idUsuario=idUser)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('andromeda:index')
#     return render(request,'usuarioDelete.html',{'user':user})
#
#
# def validate_username(request):
#     username = request.POST.get('username', None)
#     password = request.POST.get('pass',None)
#
#     acceso = authenticate(username=username,password=password)
#     if acceso is not None:
#         login(request,acceso)
#         return HttpResponse('1');
#     else:
#         return HttpResponse('0');
    # data = {
    #     'is_taken': User.objects.filter(username__iexact=username).exists()
    # }
    # if data['is_taken']:

    #     data['error_message'] = 'A user with this username already exists.'
    # lista = seralizers.seralize('Json','querySet')
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # return JsonResponse({'username': username,'pass':password})

#
# class UsuarioList(ListView):
#     model = usuario
#     template_name = 'usuarioList.html'
#
# class UsuarioCrear(CreateView):
#     model = usuario
#     form_class = UsuarioForm
#     template_name = 'registarUsuario.html'
#     success_url = reverse_lazy('andromeda:index')
#
# class TestAjax(TemplateView):
#     template_name = 'ajax.html';
#
# class UsuarioUpdate(UpdateView):
#     model = usuario
#     form_class = UsuarioForm
#     template_name = 'registarUsuario.html'
#     success_url = reverse_lazy('andromeda:index')
#
# class UsuarioDelete(DeleteView):
#     model = usuario
#     # template_name = 'registarUsuario.html'
#     success_url = reverse_lazy('andromeda:index')
#
# class RegistroUsuario(CreateView):
#     model = User
#     template_name = 'registrar.html'
#     form_class = RegistroForm
#     # success_url = reverse_lazy('andromeda:index')
