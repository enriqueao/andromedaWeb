from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required

from andromeda.views import *

urlpatterns = [
    url(r'^$',bienvenida,name='index'),
    url(r'^ayuda/$',ayuda,name='ayuda'),
    url(r'^perfil/$',perfil,name='perfil'),
    url(r'^recordatorio/$',recordatorio,name='recordatorio'),
    url(r'^andromeda/$',andromeda,name='andromeda'),
    # url(r'^usuario/$',login_required(archive),name='usuario'),
    url(r'^Usuario/$',usuario,name='principal'),
    # url(r'^usuarioUpdate/(?P<pk>\d+)',UsuarioUpdate.as_view(),name='usuarioUpdate'),
]
