from django.core.urlresolvers import resolve
from django.test import TestCase
from ropa.views import nuevo, listar, eliminar, editar
from django.http import HttpRequest
from ropa.models import Ropa, Color, TipoTela, TipoPrenda

# Create your tests here.


class MainPageRopa(TestCase):
    #################################################################
    # pruebas unitarias para probar la funcionalidad de la app ropa en su
    # opcion listar ropa

    def test_root_url_resolves_to_ropa_listar_view(self):
        found = resolve('/ropa/')
        self.assertEqual(found.func, listar)
#################################################################

    def test_ropa_listar_returns_correct_html(self):
        request = HttpRequest()
        response = listar(request)
        self.assertIn(b'<html>', response.content)
        self.assertIn(b'<h1>Lista de Prendas</h1>', response.content)
        self.assertIn(
            b'>Agregar Prenda<', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
#################################################################
    # pruebas unitarias para probar funcionalidad de la app ropa en su opcion
    # agregar ropa

    def test_root_url_resolves_to_ropa_nuevo_view(self):
        found = resolve('/ropa/nuevo/')
        self.assertEqual(found.func, nuevo)
#################################################################

    def test_ropa_nuevo_returns_correct_html(self):
        request = HttpRequest()
        response = nuevo(request)
        self.assertIn(b'<html>', response.content)
        self.assertIn(b'Prenda</h1>', response.content)
        self.assertIn(b'<input class="btn btn-warning" type="submit" value="Guardar" />',
                      response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
#################################################################
    # pruebas unitarias para probar la funcionalidad de la app ropa en su
    # opcion eliminar ropa

    def test_root_url_resolves_to_ropa_eliminar_view(self):
        found = resolve('/ropa/0/eliminar')
        self.assertEqual(found.func, eliminar)
#################################################################
    # test de prueba editado por el profesor Alejandro

    def test_ropa_eliminar_returns_correct_error_message(self):
        request = HttpRequest()
        color = Color(color='azul')
        color.save()
        colores = Color.objects.all()

        self.assertEqual(colores[0].color, 'azul')
        colores = Color.objects.all()

        self.assertEqual(len(colores), 1)

        colorDel = Color.objects.get(color='azul')
        colorDel.delete()
#################################################################

    def test_ropa_nuevo_agrega_correctamente(self):
        tipTela = TipoTela(tipoTela='Mezcliya')
        tipPrenda = TipoPrenda(tipoPrenda='Pantalon')
        tipCol = Color(color='azul')

        tipTela.save()
        tipPrenda.save()
        tipCol.save()

        tipTela = TipoTela.objects.all()
        tipPrenda = TipoPrenda.objects.all()
        tipCol = Color.objects.all()

        propie = 'Raul suarez'
        tel = 3123141
        email = 'rsuar@hotmail.com'

        '''Datos de entrega'''
        fechaRec = '2015-12-12'
        fechaEnt = '2015-12-14'
        cost = 50.00

        '''Datos de la prenda'''
        col = tipCol[0]
        tTela = tipTela[0]
        tPrenda = tipPrenda[0]

        ropa = Ropa(propietario=propie, telefono=tel, mail=email, fechaRecibo=fechaRec,
                    fechaEntrega=fechaEnt, costo=cost, tipoTela=tTela, tipoPrenda=tPrenda, color=col)
        ropa.save()
        ropa = Ropa.objects.all()
        self.assertEqual(len(ropa), 1)
#################################################################
    def test_ropa_eliminar_borra_correctamente(self):
        tipTela = TipoTela(tipoTela='Mezcliya')
        tipPrenda = TipoPrenda(tipoPrenda='Pantalon')
        tipCol = Color(color='azul')

        tipTela.save()
        tipPrenda.save()
        tipCol.save()

        tipTela = TipoTela.objects.all()
        tipPrenda = TipoPrenda.objects.all()
        tipCol = Color.objects.all()

        propie = 'Raul suarez'
        tel = 3123141
        email = 'rsuar@hotmail.com'

        '''Datos de entrega'''
        fechaRec = '2015-12-12'
        fechaEnt = '2015-12-14'
        cost = 50.00

        '''Datos de la prenda'''
        col = tipCol[0]
        tTela = tipTela[0]
        tPrenda = tipPrenda[0]

        ropa = Ropa(propietario=propie, telefono=tel, mail=email, fechaRecibo=fechaRec,
                    fechaEntrega=fechaEnt, costo=cost, tipoTela=tTela, tipoPrenda=tPrenda, color=col)
        ropa.save()
        ropa = Ropa.objects.all()
        self.assertEqual(len(ropa), 1)

        ropa[0].delete()
        ropa = Ropa.objects.all()
        self.assertEqual(len(ropa), 0)

#################################################################
    # pruebas unitarias para probar la funcionalidad de la app ropa en su
    # opcion editar ropa
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

	#test de prueba editado por el profesor Alejandro
	def test_ropa_eliminar_returns_correct_error_message(self):
		#request = HttpRequest()
		color=Color(color='azul')
		color.save()
		colores = Color.objects.all()

		self.assertEqual(colores[0].color,'azul')
		colores = Color.objects.all()

		self.assertEqual(len(colores),1)

		colorDel = Color.objects.get(color='azul')
		colorDel.delete()
