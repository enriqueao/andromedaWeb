# -*- coding:utf-8 -*_
from django.shortcuts import render,redirect
from django.template import loader,Context
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.views.generic import *
from django.core.urlresolvers import *

from andromeda.models import *
from andromeda.forms import *
# Create your views here.
def login_view(request):
    username = request.POST.get('username',False)
    password = request.POST.get('password',False)
    user = authenticate(username=username, password=password)
    print(username,password)
    if user is not None and user.is_active:
        login(request, user)
        # return HttpResponseRedirect("/n1.html")# Redirect to a success page.
        print(1)
    else:
        # return HttpResponseRedirect("/account/invalid/")# Return a 'disabled account' error message
        print(0)
    return render(request,'enter.html')

def index(request):
    form = LoginForm(request.POST or None)
    if method.request == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            nombres_usuarios = data.get('name_user')
            contrasenia_usuarios = data.get('password_user')
            acceso = authenticate(username=nombres_usuarios,password=contrasenia_usuarios)
            if acceso is not None:
                login(request,acceso)
            else:
                return HttpResponseRedirect('/andromeda')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form_login':form})

def archive(request):
    user = usuario.objects.all()
    mi_contexto = {'user':user}
    return render(request,'archive.html',mi_contexto)

def index(request):
    user = usuario.objects.filter(idUsuario = 1)
    mi_contexto = {'user':user}
    return render(request,'archive.html',mi_contexto)

def formUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('andromeda:index')
    else:
        form = UsuarioForm()

    return render(request,'registarUsuario.html',{'form':form})

def usuarioList(request):
    user = usuario.objects.all().order_by('id')
    contexto = {'user':user}
    return render(request,'listarUsuario.html',contexto)

def usuarioEditar(request,idUser):
    user = usuario.objects.get(idUsuario=idUser)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
    else:
        form =  UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('adromeda:usuario')
    return render(request,'registarUsuario.html',{'form':form})


def usuarioDelete(request,idUser):
    user = user.objects.get(idUsuario=idUser)
    if request.method == 'POST':
        user.delete()
        return redirect('andromeda:index')
    return render(request,'usuarioDelete.html',{'user':user})

def gracias(request):
    html = '<h1>Gracias</h1>'
    return HttpResponse(html)

class UsuarioList(ListView):
    model = usuario
    template_name = 'usuarioList.html'

class index(TemplateView):
    template_name = 'index.html'

class UsuarioCrear(CreateView):
    model = usuario
    form_class = UsuarioForm
    template_name = 'registarUsuario.html'
    success_url = reverse_lazy('andromeda:index')


class UsuarioUpdate(UpdateView):
    model = usuario
    form_class = UsuarioForm
    template_name = 'registarUsuario.html'
    success_url = reverse_lazy('andromeda:index')

class UsuarioDelete(DeleteView):
    model = usuario
    # template_name = 'registarUsuario.html'
    success_url = reverse_lazy('andromeda:index')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registrar.html'
    form_class = RegistroForm
    # success_url = reverse_lazy('andromeda:index')
