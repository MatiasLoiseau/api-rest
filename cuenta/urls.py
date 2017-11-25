from django.conf.urls import url
from cuenta import views

urlpatterns = [
    url(r'^$', views.cuenta_list),
    url(r'^(?P<pk>[0-9]+)/$', views.cuenta_modify),
]
