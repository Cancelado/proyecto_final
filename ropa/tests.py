from django.core.urlresolvers import resolve
from django.test import TestCase
from ropa.views import nuevo, listar, eliminar, editar
from django.http import HttpRequest
from ropa.models import Ropa, Color

# Create your tests here.                                       
class MainPageRopa(TestCase):

	#pruebas unitarias para probar la funcionalidad de la app ropa en su opcion listar ropa
	def test_root_url_resolves_to_ropa_listar_view(self):
		found = resolve('/ropa/')
		self.assertEqual(found.func, listar)

<<<<<<< HEAD

	def test_root_url_resolves_to_editar_view(self):
		found = resolve('/ropa/editar/')
		self.assertEqual(found.func, editar)
=======
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

	def test_ropa_eliminar_returns_correct_error_message(self):
		request = HttpRequest()
		color=Color(color='azul')
		color.save()
		colores = Color.objects.all()

		self.assertEqual(colores[0].color,'azul')
		colores = Color.objects.all()

		self.assertEqual(len(colores),1)

		colorDel = Color.objects.get(color='azul')
		colorDel.delete()

#		self.assertIn('Http404', response.content)

	#pruebas unitarias para probar la funcionalidad de la app ropa en su opcion editar ropa
	def test_root_url_resolves_to_ropa_editar_view(self):
		found = resolve('/ropa/1/editar/')
		self.assertEqual(found.func, editar)

	def test_ropa_editar_returns_correct_html(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['id'] = '1'
		response = editar(request)
		self.assertIn(b'Ropa</h1>', response.content)
>>>>>>> 0f5d5dd39dc435f3cb67a895c3c6035b8bdc352d
