from django.core.urlresolvers import resolve
from django.test import TestCase
from list.view import nuevo

# Create your tests here.
class MainPageRopa(TestCase):

	def test_root_url_resolves_to_nuevo_view():
		found = resolve('/listar')
		self.assertEqual(found.func, listar)