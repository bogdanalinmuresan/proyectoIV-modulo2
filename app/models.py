#from django.db import models 
	#Las tablas de la base de datos

#from mongoengine import *


#class Producto(models.Model):
#    nombre = models.CharField(max_length=50)
#    estado = models.CharField(max_length=20)

#class Usuario(models.Model):
#    nombre=models.CharField(max_length=50)
#    edad=models.IntegerField()
#    correo=models.CharField(max_length=50)
#    telefono=models.CharField(max_length=35)


#class Usuario(Document):
#	username = StringField(max_length=200,required=True)
#	email=EmailField()
#	password =StringField()

#class Post(Document):
#	author = ReferenceField(Usuario)
#	content = StringField()
#	tags = ListField(StringField(max_length=50))