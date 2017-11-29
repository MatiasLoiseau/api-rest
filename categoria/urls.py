from django.conf.urls import url
from categoria import views

urlpatterns = [
    url(r'^$', views.categoria_list),
    url(r'^(?P<pk>[0-9]+)/$', views.categoria_modify),
]
