from django.core.urlresolvers import resolve
from django.test import TestCase
from ropa.views import nuevo, listar, editar

# Create your tests here.                                       
class MainPageRopa(TestCase):

	def test_root_url_resolves_to_nuevo_view(self):
		found = resolve('/ropa/nuevo/')
		self.assertEqual(found.func, nuevo)

	def test_root_url_resolves_to_listar_view(self):
		found = resolve('/ropa/')
		self.assertEqual(found.func, listar)

	def test_root_url_resolves_to_editar_view_(self):
		found = resolve('/ropa/editar/')
		self.assertEqual(found.func, editar)