from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required

from andromeda.views import *

urlpatterns = [
    url(r'^$',bienvenida,name='index'),
    # url(r'^usuario/$',login_required(archive),name='usuario'),
    url(r'^Usuario/$',usuario,name='user'),
    # url(r'^usuarioUpdate/(?P<pk>\d+)',UsuarioUpdate.as_view(),name='usuarioUpdate'),
]
