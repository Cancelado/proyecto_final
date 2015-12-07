# coding: utf-8
from django.conf.urls import include, url
from ropa import views
from .views import listar, nuevo, eliminar, editar

urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo, name="nuevo"),
    url(r'^(?P<pk>[0-9]+)eliminar', eliminar, name="eliminar"),
    url(r'^(?P<pk>[0-9]+)editar', views.editar, name="editar"),
]