
import sys
import pymongo
from pymongo import MongoClient 
from models import *
SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]
user = {
        "nombre": "bob",
        "apellidos":"mures",
        "edad":"24" ,
        "telefono":'958582345'}


#usuario=Usuario(username='bob',email='alinugr@correo.ugr.es',password='123456')

MONGODB_URI = 'mongodb://bogdanaliniv15:ar03pbo@ds027495.mongolab.com:27495/ivdai' 

client=MongoClient(MONGODB_URI)
db=client["ivdai"]
#db.usuarios.insert_one(SEED_DATA).
usuarios=db["usuarios"]
usuarios.insert_one(user)
#usuarios.insert_one(usuario)






