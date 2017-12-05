from rest_framework.test import APITestCase
from cuenta.serializer import CuentaSerializer


class CuentaTestCase(APITestCase):
    # Test module for Cuenta model 

    def test_post_cuenta(self):
        cuenta_data = {
            "nombre": "testnombre",
        }
        response = self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        self.assertEqual(201, response.status_code)

    def test_delete_cuenta(self):
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        responseDelete = self.client.delete('/controlgastos/cuentas/1/', format='json')
        self.assertEqual(410, responseDelete.status_code)
        
    def test_put_cuenta(self):
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        cuenta_data_modificada = {
            "nombre": "testnombrecualquiera",
        }
        responsePut = self.client.put('/controlgastos/cuentas/1/', cuenta_data_modificada, format='json')
        self.assertEqual(200, responsePut.status_code)
