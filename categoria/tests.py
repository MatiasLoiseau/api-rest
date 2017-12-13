from rest_framework.test import APITestCase
from django.core.management import call_command

#TEST DEL RECURSO CATEGOGIA
class CategoriaTestCase(APITestCase):
    
    '''Alta de Categoria'''
    
    #Testeo la carga de una categoria
    def test_post_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        categoria_data = {u'nombre': u'testnombre', u'cuenta': u'1'}
        response = self.client.post('/controlgastos/categorias/', categoria_data, format='json')
        self.assertEqual(201, response.status_code)
        
   #Testeo la carga de una categoria asociada a una cuenta inexistente
    def test_bad_request_incorrect_type_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        categoria_data_wrong = {u'nombre': u'testnombre', u'cuenta': u'SoyUnError'}
        response_post_wrong = self.client.post('/controlgastos/categorias/', categoria_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)      
        
    #Testeo la carga de una categoria con parametros incorrectos
    def test_bad_request_field_required_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        categoria_data_wrong = {u'cuenta': u'ERROR'}
        response_post_wrong = self.client.post('/controlgastos/categorias/', categoria_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

   
    '''Modificacion de Categoria''' 
    
    #Testeo modificacion de una categoria
    def test_put_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        call_command('loaddata', 'data_cate.json', app_label='categoria')
        categoria_data_modificada = {u'nombre': u'testnombre', u'cuenta': u'1'}
        responsePut = self.client.put('/controlgastos/categorias/1/', categoria_data_modificada, format='json')
        self.assertEqual(200, responsePut.status_code)
        
   #Testeo modificación de categoria con envio incorrecto de parametros
    def test_bad_request_put_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')#Cargo las cuentas ya creadas
        call_command('loaddata', 'data_cate.json', app_label='categoria') #Cargo las categorias ya creadas
        categoria_data_modificada = {u'nombre': u''}
        response_put = self.client.put('/controlgastos/categorias/1/', categoria_data_modificada, format='json')
        self.assertEqual(400, response_put.status_code) 
        
        
    '''Eliminacion de Categoria'''

    #Testeo de eliminacion de categoria
    def test_delete_categoria(self):
        call_command('loaddata', 'data_acc.json', app_label='categoria')
        call_command('loaddata', 'data_cate.json', app_label='categoria')
        responseDelete = self.client.delete('/controlgastos/categorias/1/', format='json')
        self.assertEqual(200, responseDelete.status_code)
        
    #Testeo intento de eliminacion de una categoria no creada
    def test_not_found_delete_categoria_erroneo(self):
        response_delete = self.client.delete('/controlgastos/categorias/10/', format='json')
        self.assertEqual(404, response_delete.status_code)
        

 
