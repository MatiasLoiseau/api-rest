from rest_framework.test import APITestCase
from django.core.management import call_command
import json

#TEST DEL RECURSO Movimiento
class MovimientoTestCase(APITestCase):
    
    '''Alta de movimiento'''

    #Testeo creación de un movimiento
    def test_post_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        movimiento_data = {u'monto': u'20000', u'categoria': u'1', u'user': u'1'}
        response_post = self.client.post('/controlgastos/movimientos/', movimiento_data, format='json')
        self.assertEqual(201, response_post.status_code)

    #Testeo que indique Bad Request en caso de que se quiera crear un movimiento pasando parametros de tipo incorrecto
    def test_bad_request_incorrect_type_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        movimiento_data_wrong = {u'monto': u'20000', u'categoria': u'SoyUnError', u'user': u'1'}
        response_post_wrong = self.client.post('/controlgastos/movimientos/', movimiento_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

    #Testeo que no se permita la creación del movimiento si no se pasan los parametros considerados como obligatorios
    def test_bad_request_field_required_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        movimiento_data_wrong = {u'monto': u'20000', u'categoria': u'1'}
        response_post_wrong = self.client.post('/controlgastos/movimientos/', movimiento_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

    #Testeo la creacion de un movimiento asociado a una categoria inexistente
    def test_bad_request_no_encuentra_recurso_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        movimiento_data_wrong = {u'monto': u'20000', u'categoria': u'999', u'user': u'1'}
        response_post_wrong = self.client.post('/controlgastos/movimientos/', movimiento_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

    #Testeo la creacion de un movimiento asociado a un usuario inexistente
    def test_bad_request_no_encuentra_recurso_2_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        movimiento_data_wrong = {u'monto': u'20000', u'categoria': u'1', u'user': u'999'}
        response_post_wrong = self.client.post('/controlgastos/movimientos/', movimiento_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)


    '''Consulta de movimiento'''

    #Testeo la consulta de los movimientos
    def test_get_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        response = self.client.get('/controlgastos/movimientos/')
        self.assertEqual(200, response.status_code)
        
    #Testeo la consulta de un movimiento especifico
    def test_get_movimiento_bypk(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        call_command('loaddata', 'data_mov.json', app_label='movimiento') #Cargo los movimientos ya creados
        response = self.client.get('/controlgastos/movimientos/1/')
        self.assertEqual(200, response.status_code)
       

    '''Eliminacion de movimiento'''

    #Testeo borrado de un movimiento
    def test_delete_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        call_command('loaddata', 'data_mov.json', app_label='movimiento') #Cargo los movimientos ya creados
        response_delete = self.client.delete('/controlgastos/movimientos/1/', format='json')
        self.assertEqual(200, response_delete.status_code)

    #Testeo intento de borrado de un movimiento inexistente
    def test_not_found_delete_movimiento_erroneo(self):
        response_delete = self.client.delete('/controlgastos/movimientos/99/', format='json')
        self.assertEqual(404, response_delete.status_code)


    '''Modificacion de movimiento'''

    #Testeo modificación de un movimiento
    def test_put_movimiento(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        call_command('loaddata', 'data_mov.json', app_label='movimiento') #Cargo los movimientos ya creados
        movimiento_data_modificada = {u'monto': u'20000', u'categoria': u'1', u'user': u'1',u'descripcion':u'alquileres'}
        response_put = self.client.put('/controlgastos/movimientos/1/', movimiento_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)

    #Testeo modificación de un movimiento con envio incorrecto de parametros
    def test_bad_request_put_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='movimiento') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='movimiento') #Cargo los usuarios ya creados
        call_command('loaddata', 'data_cate.json', app_label='movimiento') #Cargo las categorias ya creadas
        call_command('loaddata', 'data_mov.json', app_label='movimiento') #Cargo los movimientos ya creados
        movimiento_data_modificada = {u'monto': u'20000', u'categoria': u'ERROR', u'user': u'1',u'descripcion':u'alquileres'}
        response_put = self.client.put('/controlgastos/movimientos/1/', movimiento_data_modificada, format='json')
        self.assertEqual(400, response_put.status_code)