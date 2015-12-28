from django.test import TestCase
import sys
import pymongo
from pymongo import MongoClient 
# Create your tests here.


MONGODB_URI = 'mongodb://bogdanaliniv15:ar03pbo@ds027495.mongolab.com:27495/ivdai' 
client=MongoClient(MONGODB_URI)	
db=client["ivdai"]
#db.usuarios.insert_one(SEED_DATA).
usuarios=db["usuarios"]



user = {
        "nombre": "bob",
        "apellidos":"mures",
        "edad":"24" ,
        "telefono":'958582345'}


class test(TestCase):
	#no modificar
    def testInsertarUsuario(self):
		usuarios.insert_one(user)
    	print("insercion correcta de un usuario en la BD .")


