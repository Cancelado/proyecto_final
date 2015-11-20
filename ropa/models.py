# coding: utf-8
from django.db import models

class TipoTela(models.Model):
	tipoTela = models.CharField(max_length=65)

	def __str__(self):
		return self.estado


class Color(models.Model):
	color = models.CharField(max_length=65)

	def __str__(self):
		return self.estado


class TipoPrenda(models.Model):
	tipoPrenda = models.CharField(max_length=65)

	def __str__(self):
		return self.estado


class Ropa(models.Model):
	
	'''Datos del propietario'''
	propietario = models.CharField(max_length=125)
	telefono = models.IntegerField(default=0)
	mail = models.EmailField('E-mail',max_length=60)
	
	'''Datos de entrega'''
	fechaRecibo = models.DateField('Fecha de ingreso')
	fechaEntrega = models.DateField('Fecha de entrega')
	costo = models.FloatField(default=0)
	
	'''Datos de la prenda'''
	tipoTela = models.ForeignKey(TipoTela)
	tipoPrenda = models.ForeignKey(TipoPrenda)
	color = models.ForeignKey(Color)

	def __str__(self):
		return self.estado
