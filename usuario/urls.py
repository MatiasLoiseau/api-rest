from django.conf.urls import url
from usuario import views

urlpatterns = [
    url(r'^$', views.usuario_list),
    url(r'^(?P<pk>[0-9]+)/$', views.usuario_modify)
]
