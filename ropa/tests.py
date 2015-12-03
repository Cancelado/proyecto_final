from django.core.urlresolvers import resolve
from django.test import TestCase
from ropa.views import nuevo, listar, eliminar

# Create your tests here.                                       
class MainPageRopa(TestCase):

	def test_root_url_resolves_to_ropa_nuevo_view(self):
		found = resolve('/ropa/nuevo/')
		self.assertEqual(found.func, nuevo)

	def test_root_url_resolves_to_ropa_listar_view(self):
		found = resolve('/ropa/')
		self.assertEqual(found.func, listar)

	def test_root_url_resolves_to_ropa_eliminar_view(self):
		found = resolve('^/ropa/eliminar/')
		self.assertEqual(found.func, eliminar)

	# def test_root_url_resolves_to_ropa_editar_view(self):
	#	found = resolve('/ropa/editar/')
	#	print found
	#	self.assertEqual(found.func, editar)