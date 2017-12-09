from rest_framework.test import APITestCase
from cuenta.serializer import CuentaSerializer
from categoria.serializer import CategoriaSerializer
from django.core.management import call_command


class CategoriaTestCase(APITestCase):
    # Test module for Categoria model

    def test_post_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        self.assertEqual(201, response.status_code)

    def test_delete_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        call_command('loaddata', 'data_cate.json', app_label='categoria')
        responseDelete = self.client.delete('/controlgastos/categorias/1/', format='json')
        self.assertEqual(200, responseDelete.status_code)

    def test_put_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        call_command('loaddata', 'data_cate.json', app_label='categoria')
        categoria_data_modificada = {u'nombre': u'testnombremodificado', u'cuenta': u'1'}
        responsePut = self.client.put('/controlgastos/categorias/1/', categoria_data_modificada, format='json')
        self.assertEqual(200, responsePut.status_code)
