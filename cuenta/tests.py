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

"""class IntegracionTestCase(APITestCase):
    def test_all(self):
        #Cuenta 1
        cuenta_1_data = {u'nombre': u'rodriguez'}
        response = self.client.post('/controlgastos/cuentas/', cuenta_1_data, format='json')#ID 1
        #Ccuenta 2
        cuenta_2_data = {u'nombre': u'perez'}
        response = self.client.post('/controlgastos/cuentas/', cuenta_2_data, format='json')#ID 2
        #Categorias para la cuenta 1
        categoria_cuenta_1_data_1 = {u'nombre': u'comida', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_1, format='json')#ID 1
        categoria_cuenta_1_data_2 = {u'nombre': u'reparacion auto', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_2, format='json')#ID 2
        categoria_cuenta_1_data_3 = {u'nombre': u'articulos de limpieza', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_3, format='json')#ID 3
        #Categorias para la cuenta 2
        categoria_cuenta_2_data_1 = {u'nombre': u'peluqueria', u'cuenta': u'2'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_2_data_1, format='json')#ID 4
        categoria_cuenta_2_data_2 = {u'nombre': u'casamiento', u'cuenta': u'2'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_2_data_2, format='json')#ID 5
        #Usuarios para la cuenta 1
        usuario_cuenta_1_data_1 = {u'password': u'1234', u'user': u'Miguel', u'cuenta': u'1', u'email': u'elmigue@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_1_data_1, format='json')
        usuario_cuenta_1_data_2 = {u'password': u'5678', u'user': u'Ruperta', u'cuenta': u'1', u'email': u'rupertita@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_1_data_2, format='json')
        usuario_cuenta_1_data_2 = {u'password': u'9012', u'user': u'Tito', u'cuenta': u'1', u'email': u'titoman@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_1_data_2, format='json')
        #Usuarios para la cuenta 2
        usuario_cuenta_2_data_1 = {u'password': u'1234', u'user': u'Jaime', u'cuenta': u'2', u'email': u'elmigue@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_2_data_1, format='json')
        usuario_cuenta_2_data_2 = {u'password': u'5678', u'user': u'Ruperta', u'cuenta': u'1', u'email': u'rupertita@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_2_data_2, format='json')"""