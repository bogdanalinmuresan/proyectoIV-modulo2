from django.db import models 
	#Las tablas de la base de datos

class Libro(models.Model):
	nombre = models.CharField(max_length=50) 
	fecha = models.DateField()