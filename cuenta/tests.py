from django.test import TestCase
from models import Cuenta
#from rest_framework.test import APIRequestFactory

# Create your tests here.
#factory = APIRequestFactory()
#request = factory.post('/controlgastos/cuentas/', {'nombre': 'nombrecualquiera'})




class CuentaTest(TestCase):
    """ Test module for Cuenta model """

    def setUp(self):
        Cuenta.objects.create(nombre='CuentaLoca')
        Cuenta.objects.create(nombre='OtraCuentaLoca')

    def test_cuenta_nombre(self):
        cuenta_uno = Cuenta.objects.get(nombre='CuentaLoca')
        cuenta_dos = Cuenta.objects.get(nombre='OtraCuentaLoca')
        self.assertEqual(cuenta_uno.get_name(), "CuentaLoca")
        self.assertEqual(cuenta_dos.get_name(), "OtraCuentaLoca")