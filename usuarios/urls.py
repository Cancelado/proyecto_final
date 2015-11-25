from django.conf.urls import include, url
from .views import listarU, nuevoU, eliminar, editar

urlpatterns = [
    url(r'^$', listarU, name ="listarU"),
    url(r'^nuevoU/$', nuevoU, name = "nuevoU"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar, name= "eliminar"),
    url(r'^(?P<pk>[0-9]+)/editar', editar, name= "editar"),
]