from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',  views.productos_list, name='main'),
    url(r'^consumir/(?P<pk>[A-Za-z]+)/$', views.consumir_producto, name='consumir_producto'),
]