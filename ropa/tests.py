from django.core.urlresolvers import resolve
from django.test import TestCase
from ropa.views import nuevo, listar, eliminar, editar
from django.http import HttpRequest

# Create your tests here.                                       
class MainPageRopa(TestCase):

	#pruebas unitarias para probar la funcionalidad de la app ropa en su opcion listar ropa
	def test_root_url_resolves_to_ropa_listar_view(self):
		found = resolve('/ropa/')
		self.assertEqual(found.func, listar)

	def test_ropa_listar_returns_correct_html(self):
		request = HttpRequest()
		response = listar(request)
		self.assertTrue(response.content.startswith(b'<div>'))
		self.assertIn(b'<h1>Lista de Prendas</h1>',response.content)
		self.assertIn(b'<button onclick="window.location=\'/ropa/nuevo/\'">Agregar Prenda</button>',response.content)
		self.assertTrue(response.content.endswith(b'</div>'))

	#pruebas unitarias para probar funcionalidad de la app ropa en su opcion agregar ropa
	def test_root_url_resolves_to_ropa_nuevo_view(self):
		found = resolve('/ropa/nuevo/')
		self.assertEqual(found.func, nuevo)	

	def test_ropa_nuevo_returns_correct_html(self):
		request = HttpRequest()
		response = nuevo(request)
		self.assertTrue(response.content.startswith(b'<div>'))
		self.assertIn(b'Ropa</h1>', response.content)
		self.assertIn(b'<input type="submit" value="Guardar" />', response.content)
		self.assertTrue(response.content.endswith(b'</div>'))

	#pruebas unitarias para probar la funcionalidad de la app ropa en su opcion eliminar ropa
	def test_root_url_resolves_to_ropa_eliminar_view(self):
		found = resolve('/ropa/0/eliminar')
		self.assertEqual(found.func, eliminar)

	def test_ropa_eliminar_returns_correct_html(self):
		request = HttpRequest()
		response = eliminar(request,0)
		self.assertTrue(response.content.startswith(b'<div>'))

	#pruebas unitarias para probar la funcionalidad de la app ropa en su opcion editar ropa
	def test_root_url_resolves_to_ropa_editar_view(self):
		found = resolve('/ropa/1/editar/')
		self.assertEqual(found.func, editar)

	#def test_ropa_editar_returns_correct_html(self):
	#	request = HttpRequest()
	#	response = editar(request)
	#	self.assertTrue(response.content.startswith(b'<div>'))