from django.conf.urls import include, url
from .views import listarU, nuevoU, eliminarU, editarU

urlpatterns = [
    url(r'^$', listarU, name ="listarU"),
    url(r'^nuevoU/$', nuevoU, name = "nuevoU"),
    url(r'^(?P<pk>[0-9]+)/eliminarU', eliminarU, name= "eliminarU"),
    url(r'^(?P<pk>[0-9]+)/editarU', editarU, name= "editarU"),
]