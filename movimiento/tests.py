from rest_framework.test import APITestCase


class MovimientoTestCase(APITestCase):
    # Test module for Movimiento model 

    def test_post_movimiento(self):
    	#Creo una cuenta para la categoria
        cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        categoria_data = {
            "nombre": "testnombre",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        movimiento_data = {
        	"monto": "20000",
            "categoria": "1",
            "user": "1",
        }
        response_post = self.client.post('/controlgastos/movimientos/', movimiento_data, format='json')
        self.assertEqual(201, response_post.status_code)
        
       
    def test_delete_movimiento(self):
    	#Creo una cuenta para la categoria
        cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        categoria_data = {
            "nombre": "testnombre",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        movimiento_data = {
        	"monto": "20000",
            "categoria": "1",
            "user": "1",
        }
        response_post = self.client.post('/controlgastos/movimientos/', movimiento_data, format='json')
        response_delete = self.client.delete('/controlgastos/movimientos/1/', format='json')
        self.assertEqual(410, response_delete.status_code)
        
    def test_put_movimiento(self):
    	#Creo una cuenta para la categoria
        cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        categoria_data = {
            "nombre": "testnombre",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        movimiento_data = {
        	"monto": "20000",
            "categoria": "1",
            "user": "1",
        }
        movimiento_data_modificada = {
        	"monto": "999999",
            "categoria": "1",
            "user": "1",
        }
        response_post = self.client.post('/controlgastos/movimientos/', movimiento_data, format='json')
        response_put = self.client.put('/controlgastos/movimientos/1/', movimiento_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)


