from rest_framework.test import APITestCase
from django.core.management import call_command


class CuentaTestCase(APITestCase):
    # Test module for Cuenta model

    def test_post_cuenta(self):
        cuenta_data = {u'nombre': u'testnombre'}
        response = self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        self.assertEqual(201, response.status_code)

    def test_delete_cuenta(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta')
        responseDelete = self.client.delete('/controlgastos/cuentas/1/', format='json')
        self.assertEqual(200, responseDelete.status_code)

    def test_put_cuenta(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta')
        cuenta_data_modificada = {u'nombre': u'testnombremodificado'}
        responsePut = self.client.put('/controlgastos/cuentas/1/', cuenta_data_modificada, format='json')
        self.assertEqual(200, responsePut.status_code)

    def test_bad_request_field_required_cuenta(self):
        cuenta_data_wrong = {}
        response_post_wrong = self.client.post('/controlgastos/cuentas/', cuenta_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)
