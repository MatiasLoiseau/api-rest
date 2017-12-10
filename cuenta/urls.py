from django.conf.urls import url
from cuenta import views
from usuario import views as viewsu
from categoria import views as viewsc

urlpatterns = [
    url(r'^$', views.cuenta_list),
    url(r'^(?P<pk>[0-9]+)/$', views.cuenta_modify),
    url(r'^(?P<pk>[0-9]+)/usuarios/$', viewsu.usuario_get),
    url(r'^(?P<pk>[0-9]+)/categorias/$', viewsc.categoria_get)
]
