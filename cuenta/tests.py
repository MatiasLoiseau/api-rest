import json
from django.test import TestCase
from models import Cuenta
#from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

# Create your tests here.
#factory = APIRequestFactory()
#request = factory.post('/controlgastos/cuentas/', {'nombre': 'nombrecualquiera'})


class CuentaTestCase(APITestCase):
    # Test module for Cuenta model 

    def test_post_cuenta(self):
        cuenta_data = {
            "nombre": "testnombre",
        }
        response = self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        self.assertEqual(201, response.status_code)

    def test_delete_cuenta(self):
        cuenta_data = {
            "nombre": "testnombrecualquiera",
        }
        response2 = self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        response3 = self.client.delete('/controlgastos/cuentas/1/', format='json')
        self.assertEqual(410, response3.status_code)
        
    def test_put_cuenta(self):
        cuenta_data = {
            "nombre": "testnombrecualquiera",
        }
        cuenta_data_modificada = {
            "nombre": "testnombrecualquiera",
        }
        response2 = self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        response3 = self.client.put('/controlgastos/cuentas/1/', cuenta_data_modificada, format='json')
        self.assertEqual(200, response3.status_code)
