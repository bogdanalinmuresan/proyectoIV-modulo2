from django.db import models 
	#Las tablas de la base de datos

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    correo=models.CharField(max_length=50)
    telefono=models.CharField(max_length=35)
