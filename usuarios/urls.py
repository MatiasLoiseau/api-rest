from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^usuarios/$', views.usuarios_list),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.usuarios_detail),
]
