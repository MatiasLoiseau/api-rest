from rest_framework.test import APITestCase


class UsuarioTestCase(APITestCase):
    # Test module for Cuenta model 

    def test_post_usuario(self):
        cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        response_post = self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        self.assertEqual(201, response_post.status_code)
        
       
    def test_delete_usuario(self):
    	cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        response_delete = self.client.delete('/controlgastos/usuarios/1/', format='json')
        self.assertEqual(410, response_delete.status_code)
        
    def test_put_usuario(self):
    	cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        usuario_data_modificada = {
            "user": "testotrouser",
            "password": "testotropassword",
            "email": "testotro@email.com",
            "cuenta": "1",
        }
        self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        response_put = self.client.put('/controlgastos/usuarios/1/', usuario_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)


