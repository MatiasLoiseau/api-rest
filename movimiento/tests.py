from rest_framework.test import APITestCase
from cuenta.serializer import CuentaSerializer
from categoria.serializer import CategoriaSerializer
from usuario.serializer import UsuarioSerializer
from movimiento.serializer import MovimientoSerializer


class MovimientoTestCase(APITestCase):
    # Test module for Movimiento model 

    def test_post_movimiento(self):
    	#Creo una cuenta para la categoria
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        #Creo una categoria
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        serializerCategoria = CategoriaSerializer(data=categoria_data)
        if serializerCategoria.is_valid():
            serializerCategoria.save()
        #Creo un usuario
        usuario_data = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        serializerUsuario = UsuarioSerializer(data=usuario_data)
        if serializerUsuario.is_valid():
            serializerUsuario.save()
        movimiento_data = {
        	"monto": "20000",
            "categoria": "1",
            "user": "1",
        }
        response_post = self.client.post('/controlgastos/movimientos/', movimiento_data, format='json')
        self.assertEqual(201, response_post.status_code)
        
       
    def test_delete_movimiento(self):
    	#Creo una cuenta para la categoria
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        #Creo una categoria
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        serializerCategoria = CategoriaSerializer(data=categoria_data)
        if serializerCategoria.is_valid():
            serializerCategoria.save()
        #Creo un usuario
        usuario_data = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        serializerUsuario = UsuarioSerializer(data=usuario_data)
        if serializerUsuario.is_valid():
            serializerUsuario.save()
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
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        serializerCategoria = CategoriaSerializer(data=categoria_data)
        if serializerCategoria.is_valid():
            serializerCategoria.save()
        usuario_data = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        serializerUsuario = UsuarioSerializer(data=usuario_data)
        if serializerUsuario.is_valid():
            serializerUsuario.save()
        movimiento_data = {u'monto': u'20000', u'categoria': u'1', u'user': u'1'}
        serializerMovimiento = MovimientoSerializer(data=movimiento_data)
        if serializerMovimiento.is_valid():
            serializerMovimiento.save()
        movimiento_data_modificada = {
        	"monto": "999999",
            "categoria": "1",
            "user": "1",
        }
        response_put = self.client.put('/controlgastos/movimientos/1/', movimiento_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)


