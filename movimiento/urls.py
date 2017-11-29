from django.conf.urls import url
from movimiento import views

urlpatterns = [
    url(r'^$', views.movimiento_list),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.movimiento_get),
    url(r'^(?P<pk>[0-9]+)/$', views.movimiento_modify)
]
