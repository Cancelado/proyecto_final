from django.core.urlresolvers import resolve
from django.test import TestCase
from usuarios.views import nuevoU, listarU, eliminarU, editarU
from django.http import HttpRequest
from usuarios.models import Usuario

class MainPageRopa(TestCase):

	def test_root_url_resolves_to_usuarios_nuevo_view(self):
		found = resolve('/usuarios/nuevoU/')
		self.assertEqual(found.func, nuevoU)

	def test_usuario_nuevo_returns_correct_html(self):
		request = HttpRequest()
		response = nuevoU(request)
		self.assertTrue(response.content.startswith(b'<div>'))
		self.assertIn(b'<h1> Nuevo Usuario</h1>',response.content)
		self.assertIn(b'<input type = "submit" value = "Guardar" />', response.content)
		self.assertTrue(response.content.endswith(b'</div>'))

	def test_root_url_resolves_to_usuarios_listar_view(self):
		found = resolve('/usuarios/')
		self.assertEqual(found.func, listarU)

	def test_root_url_resolves_to_usuarios_eliminar_view(self):
		found = resolve('/usuarios/0/eliminarU')
		self.assertEqual(found.func, eliminarU)

	def test_root_url_resolves_to_usuarios_editar_view(self):
		found = resolve('/usuarios/1/editarU/')
		self.assertEqual(found.func, editarU)

	def test_usuario_eliminar_returns_correct_error_message(self):
		usuario=Usuario(usuario='Luis',password='nomames',nombre='Luis',apellidos='Correa Rada',fecha='2012-12-12',edad=30,mail='rada.lmc@gmail.com')
		usuario.save()
		usuarios = Usuario.objects.all()
		self.assertEqual(usuarios[0].usuario,'Luis')
		usuarios = Usuario.objects.all()
		self.assertEqual(len(usuarios),1)
		usuarioDel = Usuario.objects.get(usuario='Luis')
		usuarioDel.delete()