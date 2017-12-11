from rest_framework.test import APITestCase

class IntegracionTestCase(APITestCase):

    def test_all(self):
        #Cuenta 1
        cuenta_1_data = {u'nombre': u'rodriguez'}
        response = self.client.post('/controlgastos/cuentas/', cuenta_1_data, format='json')#ID 1
        self.assertEqual(201, response.status_code)

        #Ccuenta 2
        cuenta_2_data = {u'nombre': u'perez'}
        response = self.client.post('/controlgastos/cuentas/', cuenta_2_data, format='json')#ID 2
        self.assertEqual(201, response.status_code)

        #Categorias para la cuenta 1
        categoria_cuenta_1_data_1 = {u'nombre': u'comida', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_1, format='json')#ID 1
        self.assertEqual(201, response.status_code)
        categoria_cuenta_1_data_2 = {u'nombre': u'reparacion auto', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_2, format='json')#ID 2
        self.assertEqual(201, response.status_code)
        categoria_cuenta_1_data_3 = {u'nombre': u'articulos de limpieza', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_3, format='json')#ID 3
        self.assertEqual(201, response.status_code)

        #Categorias para la cuenta 2
        categoria_cuenta_2_data_1 = {u'nombre': u'peluqueria', u'cuenta': u'2'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_2_data_1, format='json')#ID 4
        self.assertEqual(201, response.status_code)
        categoria_cuenta_2_data_2 = {u'nombre': u'casamiento', u'cuenta': u'2'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_2_data_2, format='json')#ID 5
        self.assertEqual(201, response.status_code)

        #Usuarios para la cuenta 1
        usuario_cuenta_1_data_1 = {u'password': u'1234', u'user': u'Miguel', u'cuenta': u'1', u'email': u'elmigue@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_1_data_1, format='json')#ID 1
        self.assertEqual(201, response.status_code)
        usuario_cuenta_1_data_2 = {u'password': u'5678', u'user': u'Ruperta', u'cuenta': u'1', u'email': u'rupertita@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_1_data_2, format='json')#ID 2
        self.assertEqual(201, response.status_code)
        usuario_cuenta_1_data_2 = {u'password': u'9012', u'user': u'Tito', u'cuenta': u'1', u'email': u'titoman@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_1_data_2, format='json')#ID 3
        self.assertEqual(201, response.status_code)
        
        #Usuarios para la cuenta 2
        usuario_cuenta_2_data_1 = {u'password': u'3456', u'user': u'Jaime', u'cuenta': u'2', u'email': u'elmigue@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_2_data_1, format='json')#ID 4
        self.assertEqual(201, response.status_code)
        usuario_cuenta_2_data_2 = {u'password': u'7890', u'user': u'Fede', u'cuenta': u'2', u'email': u'fedetano@email.com'}
        response = self.client.post('/controlgastos/usuarios/', usuario_cuenta_2_data_2, format='json')#ID 5
        self.assertEqual(201, response.status_code)
        
        #Movimientos de la cuenta 1
        movimiento_cuenta_1_data_1 = {u'monto': u'200', u'categoria': u'1', u'user': u'1'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_1_data_1, format='json')#ID 1
        self.assertEqual(201, response.status_code)
        movimiento_cuenta_1_data_2 = {u'monto': u'100', u'categoria': u'1', u'user': u'1',u'descripcion':u'asado'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_1_data_2, format='json')#ID 2
        self.assertEqual(201, response.status_code)
        movimiento_cuenta_1_data_3 = {u'monto': u'7800', u'categoria': u'3', u'user': u'3'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_1_data_3, format='json')#ID 3
        self.assertEqual(201, response.status_code)
        
        #Movimientos de la cuenta 2
        movimiento_cuenta_2_data_1 = {u'monto': u'333', u'categoria': u'5', u'user': u'5'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_2_data_1, format='json')#ID 4
        self.assertEqual(201, response.status_code)
        movimiento_cuenta_2_data_2 = {u'monto': u'444', u'categoria': u'5', u'user': u'4',u'descripcion':u'flores'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_2_data_2, format='json')#ID 5
        self.assertEqual(201, response.status_code)
        movimiento_cuenta_2_data_3 = {u'monto': u'654', u'categoria': u'4', u'user': u'4'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_2_data_3, format='json')#ID 6
        self.assertEqual(201, response.status_code)
        
        #Creo nueva categoria para cuenta 1
        categoria_cuenta_1_data_4 = {u'nombre': u'electronica', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_cuenta_1_data_4, format='json')#ID 6
        self.assertEqual(201, response.status_code)
        
        #Nuevos movimientos para la nueva categoria
        movimiento_cuenta_1_data_4 = {u'monto': u'30000', u'categoria': u'6', u'user': u'2'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_1_data_4, format='json')#ID 7
        self.assertEqual(201, response.status_code)
        
        #Eliminar movimientos
        response_delete = self.client.delete('/controlgastos/movimientos/3/', format='json')#No esta mas el ID 3 de movimientos
        self.assertEqual(200, response_delete.status_code)
        
        #Nuevos movimientos para la nueva categoria
        movimiento_cuenta_1_data_5 = {u'monto': u'200', u'categoria': u'6', u'user': u'2'}
        response = self.client.post('/controlgastos/movimientos/', movimiento_cuenta_1_data_5, format='json')#ID 8
        self.assertEqual(201, response.status_code)
        
        #Modifico el anterior movimiento
        movimiento_data_modificada = {u'monto': u'200000', u'categoria': u'6', u'user': u'2',u'descripcion':u'error de tipeo'}
        response_put = self.client.put('/controlgastos/movimientos/8/', movimiento_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)
        
        #put al ID 3 --> debería ser error
        movimiento_data_modificada_2 = {u'monto': u'100', u'categoria': u'3', u'user': u'3',u'descripcion':u'SoyUnError'}
        response_put_2 = self.client.put('/controlgastos/movimientos/3/', movimiento_data_modificada_2, format='json')
        self.assertEqual(404, response_put_2.status_code)
        