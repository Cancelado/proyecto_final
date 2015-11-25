# coding: utf-8
from django import forms
from ropa.models import Ropa, Color, TipoPrenda, TipoTela

class RopaForm(forms.ModelForm):

	class Meta(object):
		model = Ropa
		fields = ['propietario', 'telefono','mail','fechaRecibo','fechaEntrega','costo','tipoTela','tipoPrenda','color']

class ColorForm(forms.ModelForm):

	class Meta(object):
		model = Color
		fields = ['color']

class TipoPrendaForm(forms.ModelForm):

	class Meta(object):
		model = TipoPrenda
		fields = ['tipoPrenda']


class TipoTelaForm(forms.ModelForm):

	class Meta(object):
		model = TipoTela
		fields = ['tipoTela']