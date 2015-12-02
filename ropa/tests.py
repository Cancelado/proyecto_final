from django.core.urlresolvers import resolve
from django.test import TestCase
from ropa.views import nuevo , listar

# Create your tests here.                                       
class MainPageRopa(TestCase):

	def test_root_url_resolves_to_nuevo_view(self):
		found = resolve('/ropa/nuevo/')
		self.assertEqual(found.func, nuevo)