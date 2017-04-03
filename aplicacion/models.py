from django.db import models
from django.core.urlresolvers import reverse

class Materia(models.Model):
	nombre_materia=models.CharField(max_length=100,blank=True)
	docente=models.CharField(max_length=100,blank=True)
	
	def __str__(self):
		return self.nombre_materia+" "+self.docente

class Estudiante(models.Model):
	"""estudiantes"""
	nombre=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	correo=models.EmailField(max_length=50)
	cedula=models.CharField(max_length=200,blank=True)
	fecha_nacimiento=models.DateField(auto_now_add=False)

	
	def __str__(self):
		return self.nombre+" "+self.apellidos

