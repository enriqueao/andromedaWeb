"""andromedaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login
from django.conf import settings

from andromeda.views import *

urlpatterns = [
    # url(r'^',login,{'template_name':'andromeda/templates/login.html'},name='login'),
    # url(r'^$', login_view),
    url(r'^', include('andromeda.urls',namespace='andromedaP')),
    url(r'^logout/',logout_then_login,name='logout'),
    url(r'^accounts/login/',login,{'template_name':'index.html'}),
    # url(r'^',login,{'template_name':'login.hml'},name='login'),
    # url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^andromeda/',include('andromeda.urls',namespace='andromeda')),
    url(r'^server/admin/', admin.site.urls),
]
