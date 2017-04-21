from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required

from andromeda.views import *



urlpatterns = [
    url(r'^',index,name='index'),
    url(r'^usuario/',login_required(archive),name='usuario'),
    url(r'^registroUsuario/',formUsuario,name='registroUsuario'),
    url(r'^listarUsuario/',UsuarioList.as_view(),name='listarUsuario'),
    url(r'^usuarioCreate/',UsuarioCrear.as_view(),name='usuarioCreate'),
    url(r'^registro/',RegistroUsuario.as_view(),name='registro'),
    # url(r'^usuarioUpdate/(?P<pk>\d+)',UsuarioUpdate.as_view(),name='usuarioUpdate'),
    # url(r'^UsuarioDelete/(?P<pk>\d+)',UsuarioDelete.as_view(),name='usuarioDelete'),
    # url(r'^editarUsuario/(?P<idUser>\d+)/',usuarioEditar,name='editarUsuario'),
    # url(r'^deleteUsuario/(?P<idUser>\d+)/',usuarioDelete,name='deleteUsuario'),
]
