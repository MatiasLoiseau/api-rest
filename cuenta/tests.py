from rest_framework.test import APITestCase
from django.core.management import call_command
import json

#TEST DEL RECURSO CUENTA
class CuentaTestCase(APITestCase):
    # Test module for Cuenta model

    '''Alta de usuario'''

    #Testeo creación de una cuenta
    def test_post_cuenta(self):
        cuenta_data = {u'nombre': u'testnombre'}
        response = self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        self.assertEqual(201, response.status_code)

    #Testeo que no se permita la creación de la cuenta si no se pasan los parametros considerados como obligatorios
    def test_bad_request_field_required_cuenta(self):
        cuenta_data_wrong = {}
        response_post_wrong = self.client.post('/controlgastos/cuentas/', cuenta_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

    '''Consulta de cuentas'''

    #Testeo la consulta de las cuentas
    def test_get_cuenta(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta') #Cargo las cuentas ya creadas
        response = self.client.get('/controlgastos/cuentas/')
        self.assertEqual(200, response.status_code)
        
    #Testeo la consulta de una cuenta en especifica
    def test_get_cuenta_bypk(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta') #Cargo las cuentas ya creadas
        response = self.client.get('/controlgastos/cuentas/1/')
        self.assertEqual(200, response.status_code)

    '''Eliminacion de una cuenta'''

    #Testeo borrado de una cuenta
    def test_delete_cuenta(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta')
        responseDelete = self.client.delete('/controlgastos/cuentas/1/', format='json')
        self.assertEqual(200, responseDelete.status_code)

    #Testeo intento de borrado de una cuenta inexistente
    def test_not_found_delete_cuenta_erronea(self):
        response_delete = self.client.delete('/controlgastos/cuentas/99/', format='json')
        self.assertEqual(404, response_delete.status_code)

    '''Modificacion de una cuenta'''

    #Testeo modificación de una cuenta
    def test_put_cuenta(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta')
        cuenta_data_modificada = {u'nombre': u'testnombremodificado'}
        responsePut = self.client.put('/controlgastos/cuentas/1/', cuenta_data_modificada, format='json')
        self.assertEqual(200, responsePut.status_code)

    #Testeo modificación de una cuenta con envio incorrecto de parametros
    def test_bad_request_put_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='cuenta') #Cargo las cuentas ya creadas
        cuenta_data_modificada = {}
        response_put = self.client.put('/controlgastos/cuentas/1/', cuenta_data_modificada, format='json')
        self.assertEqual(400, response_put.status_code)
