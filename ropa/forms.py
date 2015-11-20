# coding: utf-8
from django import forms
from ropa.models import Ropa

class RopaForm(forms.ModelForm):
	""" Formulario para dar servicio al modelo Usuario"""

	class Meta(object):
		model = Ropa
		fields = ['propietario', 'telefono','mail','fechaRecibo','fechaEntrega','costo','tipoTela','tipoPrenda','color']