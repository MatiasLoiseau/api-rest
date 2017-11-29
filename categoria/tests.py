from rest_framework.test import APITestCase


class CategoriaTestCase(APITestCase):
    # Test module for Categoria model 

    def test_post_categoria(self):
    	cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        categoria_data = {
            "nombre": "testnombre",
            "cuenta": "1",
        }
        response = self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        self.assertEqual(201, response.status_code)

    def test_delete_categoria(self):
        cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        categoria_data = {
            "nombre": "testnombre",
            "cuenta": "1",
        }
        response2 = self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        response3 = self.client.delete('/controlgastos/categorias/1/', format='json')
        self.assertEqual(410, response3.status_code)
        
    def test_put_categoria(self):
    	cuenta_data = {
            "nombre": "testnombre",
        }
        self.client.post('/controlgastos/cuentas/', cuenta_data, format='json')
        categoria_data = {
            "nombre": "testnombrecualquiera",
            "cuenta": "1",
        }
        categoria_data_modificada = {
            "nombre": "testnombrecualquiera",
            "cuenta": "1",
        }
        response2 = self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        response3 = self.client.put('/controlgastos/categorias/1/', categoria_data_modificada, format='json')
        self.assertEqual(200, response3.status_code)
