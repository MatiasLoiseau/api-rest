from rest_framework.test import APITestCase
from cuenta.serializer import CuentaSerializer
from categoria.serializer import CategoriaSerializer
from usuario.serializer import UsuarioSerializer
from movimiento.serializer import MovimientoSerializer
from django.core.management import call_command

class MovimientoTestCase(APITestCase):
    # Test module for Movimiento model
    def test_post_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento')
        call_command('loaddata', 'data_usr.json', app_label='movimiento')
        call_command('loaddata', 'data_cate.json', app_label='movimiento')
        movimiento_data = {u'monto': u'20000', u'categoria': u'1', u'user': u'1'}
        response_post = self.client.post('/controlgastos/movimientos/', movimiento_data, format='json')
        self.assertEqual(201, response_post.status_code)


    def test_delete_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento')
        call_command('loaddata', 'data_usr.json', app_label='movimiento')
        call_command('loaddata', 'data_cate.json', app_label='movimiento')
        call_command('loaddata', 'data_mov.json', app_label='movimiento')
        response_delete = self.client.delete('/controlgastos/movimientos/1/', format='json')
        self.assertEqual(200, response_delete.status_code)

    def test_put_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento')
        call_command('loaddata', 'data_usr.json', app_label='movimiento')
        call_command('loaddata', 'data_cate.json', app_label='movimiento')
        call_command('loaddata', 'data_mov.json', app_label='movimiento')
        movimiento_data_modificada = {u'monto': u'20000', u'categoria': u'1', u'user': u'1',u'descripcion':u'alquileres'}
        response_put = self.client.put('/controlgastos/movimientos/1/', movimiento_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)
