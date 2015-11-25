from django.db import models

class Usuario(models.Model):
	usuario = models.CharField(max_length=25)
	password = models.CharField(max_length=25)
	nombre = models.CharField(max_length=65)
	apellidos = models.CharField(max_length=125)
	fecha = models.DateField('Fecha de Nacimiento')
	edad = models.IntegerField(default=0)
	mail = models.EmailField('E-mail',max_length=60)

	def __unicode__(self):
		return self.nombre+" "+ self.apellidos