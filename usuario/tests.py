from rest_framework.test import APITestCase
from cuenta.serializer import CuentaSerializer
from usuario.serializer import UsuarioSerializer


class UsuarioTestCase(APITestCase):
    # Test module for Cuenta model 

    def test_post_usuario(self):
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        usuario_data = {
            "user": "testuser",
            "password": "testpassword",
            "email": "test@email.com",
            "cuenta": "1",
        }
        response_post = self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        self.assertEqual(201, response_post.status_code)
        
       
    def test_delete_usuario(self):
    	cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
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
    	cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        usuario_data = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        serializerUsuario = UsuarioSerializer(data=usuario_data)
        if serializerUsuario.is_valid():
            serializerUsuario.save()
        usuario_data_modificada = {
            "user": "testotrouser",
            "password": "testotropassword",
            "email": "testotro@email.com",
            "cuenta": "1",
        }
        response_put = self.client.put('/controlgastos/usuarios/1/', usuario_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)


