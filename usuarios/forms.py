# coding: utf-8
from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
	""" Formulario para dar servicio al modelo Usuario"""
	password = forms.CharField(widget=forms.PasswordInput, label=u'Contraseña')

	class Meta(object):
		model = Usuario
		fields = ['usuario', 'password','nombre','apellidos','fecha','mail','edad']