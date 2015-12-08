# coding: utf-8
from django.conf.urls import include, url
from ropa import views
from .views import listar, nuevo, eliminar, editar
from .views import listarColor, nuevoColor, eliminarColor, eliminar_post_color, editarColor
from .views import listarTipoPrenda, nuevoTipoPrenda, eliminarTipoPrenda, eliminar_post_TipoPrenda, editarTipoPrenda
from .views import listarTipoTela, nuevoTipoTela, eliminarTipoTela, editarTipoTela

urlpatterns = [
	
	url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo, name="nuevo"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar, name="eliminar"),
    url(r'^(?P<pk>[0-9]+)/editar', views.editar, name="editar"),

    #Color
    url(r'^listarColor', listarColor),
    url(r'^nuevoColor/', nuevoColor),
    url(r'^(?P<pk>[0-9]+)/eliminarColor', eliminarColor, name="eliminarColor"),
    url(r'^(?P<pk>[0-9]+)/editarColor', views.editarColor),

    #Tipo tela
    url(r'^listarTipoTela', listarTipoTela),
    url(r'^nuevoTipoTela/',nuevoTipoTela),
    url(r'^(?P<pk>[0-9]+)/eliminarTipoTela', eliminarTipoTela),
    url(r'^(?P<pk>[0-9]+)/editarTipoTela', views.editarTipoTela),
    
    #Tipo Prenda
    url(r'^listarTipoPrenda', listarTipoPrenda),
    url(r'^nuevoTipoPrenda/', nuevoTipoPrenda),
    url(r'^(?P<pk>[0-9]+)/eliminarTipoPrenda', eliminarTipoPrenda),
    url(r'^(?P<pk>[0-9]+)/editarTipoPrenda', views.editarTipoPrenda),
]