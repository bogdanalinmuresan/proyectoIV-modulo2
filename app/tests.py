from django.test import TestCase

# Create your tests here.

from app.models import Producto
from app.models import Usuario

class test(TestCase):
    def test(self):
        user = Usuario(nombre='alin' ,edad='24',correo='alinugr@gmail.com',telefono='958608344')
        self.assertEqual(user.nombre,'alin')
        self.assertEqual(user.edad,'24')
        self.assertEqual(user.correo,'alinugr@gmail.com')
        self.assertEqual(user.telefono,'958608344')
        print("ha pasado el test correctamente .")