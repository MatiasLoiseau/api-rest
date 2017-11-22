"""tp URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from cuentas import views as cuentas_views
from usuarios import views as usuarios_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #r'' significa que es una expresion regular y ^$ es ima expresion vacia
    #En esta linea de codigo es cuando pido la url vacia, que me ejecute la funcion home
    url(r'^$', cuentas_views.home),
    url(r'^usuarios/', usuarios_views.usuarios_list),

    #url(r'^', include('usuarios.urls', namespace='usuarios')),
    #url(r'^', include('cuentas.urls', namespace='cuentas')),
]
