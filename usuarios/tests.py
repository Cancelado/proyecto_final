from django.core.urlresolvers import resolve
from django.test import TestCase
from usuarios.views import nuevoU, listarU, eliminarU, editarU

class MainPageRopa(TestCase):

	def test_root_url_resolves_to_usuarios_nuevo_view(self):
		found = resolve('/usuarios/nuevoU/')
		self.assertEqual(found.func, nuevoU)

	def test_root_url_resolves_to_usuarios_listar_view(self):
		found = resolve('/usuarios/')
		self.assertEqual(found.func, listarU)

	def test_root_url_resolves_to_usuarios_eliminar_view(self):
		found = resolve('/usuarios/0/eliminarU')
		self.assertEqual(found.func, eliminarU)

	def test_root_url_resolves_to_usuarios_editar_view(self):
		found = resolve('/usuarios/1/editarU/')
		self.assertEqual(found.func, editarU)