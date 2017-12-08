from rest_framework.test import APITestCase
from cuenta.serializer import CuentaSerializer
from categoria.serializer import CategoriaSerializer


class CategoriaTestCase(APITestCase):
    # Test module for Categoria model 

    def test_post_categoria(self):
    	cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        categoria_data = {
            "nombre": "testnombre",
            "cuenta": "1",
        }
        response = self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        self.assertEqual(201, response.status_code)

    def test_delete_categoria(self):
        cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        serializerCategoria = CategoriaSerializer(data=categoria_data)
        if serializerCategoria.is_valid():
            serializerCategoria.save()
        responseDelete = self.client.delete('/controlgastos/categorias/1/', format='json')
        self.assertEqual(200, responseDelete.status_code)
        
    def test_put_categoria(self):
    	cuenta_data = {u'nombre': u'testnombre'}
        serializerCuenta = CuentaSerializer(data=cuenta_data)
        if serializerCuenta.is_valid():
            serializerCuenta.save()
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        serializerCategoria = CategoriaSerializer(data=categoria_data)
        if serializerCategoria.is_valid():
            serializerCategoria.save()
        categoria_data_modificada = {
            "nombre": "testnombrecualquiera",
            "cuenta": "1",
        }
        responsePut = self.client.put('/controlgastos/categorias/1/', categoria_data_modificada, format='json')
        self.assertEqual(200, responsePut.status_code)
