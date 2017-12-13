from rest_framework.test import APITestCase
from django.core.management import call_command
import json

#TEST DEL RECURSO USUARIO
class UsuarioTestCase(APITestCase):
    
    '''Alta de usuario'''
    
    #Testeo creación de un usuario
    def test_post_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        usuario_data = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        response_post = self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        self.assertEqual(201, response_post.status_code)
        
    #Testeo que indique Bad Request en caso de que se quiera crear un usuario pasando parametros de tipo incorrecto
    def test_bad_request_incorrect_type_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        usuario_data_wrong = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'SoyUnError', u'email': u'test@email.com'}
        response_post_wrong = self.client.post('/controlgastos/usuarios/', usuario_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)
        
    #Testeo que no se permita la creación del usuario si no se pasan los parametros considerados como obligatorios
    def test_bad_request_field_required_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        usuario_data_wrong = {u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        response_post_wrong = self.client.post('/controlgastos/usuarios/', usuario_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)
        
    #Testeo la creacion de un usuario asociado a una cuenta inexistente
    def test_bad_request_no_encuentra_recurso_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas
        usuario_data_wrong = {u'user': u'testuser', u'cuenta': u'99', u'email': u'test@email.com'}
        response_post_wrong = self.client.post('/controlgastos/usuarios/', usuario_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)
        
        
    '''Consulta de usuario'''
    
    #Testeo la consulta de los usuarios
    def test_get_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='usuario') #Cargo un usuario ya creado
        response = self.client.get('/controlgastos/usuarios/')
        self.assertEqual(200, response.status_code)
        
    #Testeo consulta de usuario inexistente
    def test_not_found_get_usuario(self):
        response = self.client.get('/controlgastos/usuarios/3/')
        self.assertEqual(404, response.status_code)
        
    #Testeo la consulta de un usuario especifico
    def test_get_usuario_bypk(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='usuario') #Cargo un usuario ya creado
        response = self.client.get('/controlgastos/usuarios/1/')
        self.assertEqual(200, response.status_code)
       
   #Test consulta de usuarios asociados a una cuenta x
    def test_get_usuarios_por_cuenta(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='usuario') #Cargo un usuario ya creado
        response = self.client.get('/controlgastos/cuentas/1/usuarios/')
        self.assertEqual(200, response.status_code)    
        
        
    '''Eliminacion de usuario'''
    
    #Testeo borrado de un usuario
    def test_delete_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='usuario') #Cargo un usuario ya creado
        response_delete = self.client.delete('/controlgastos/usuarios/1/', format='json')
        self.assertEqual(200, response_delete.status_code)
        
    #Testeo intento de borrado de un usuario inexistente
    def test_not_found_delete_usuario_erroneo(self):
        response_delete = self.client.delete('/controlgastos/usuarios/6/', format='json')
        self.assertEqual(404, response_delete.status_code)
        
        
    '''Modificacion de usuario'''
    
    #Testeo modificación de un usuario
    def test_put_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='usuario') #Cargo un usuario ya creado
        usuario_data_modificada = {u'password': u'testpassword2', u'user2': u'testuser', u'cuenta': u'1',u'email': u'test@email.com'}
        response_put = self.client.put('/controlgastos/usuarios/1/', usuario_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)
     
    #Testeo modificación de un usuario con envio incorrecto de parametros
    def test_bad_request_put_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario') #Cargo las cuentas ya creadas
        call_command('loaddata', 'data_usr.json', app_label='usuario') #Cargo un usuario ya creado
        usuario_data_modificada = {u'password': u'testpassword2', u'user2': u'testuser', u'cuenta': u'ERROR',u'email': u'test@email.com'}
        response_put = self.client.put('/controlgastos/usuarios/1/', usuario_data_modificada, format='json')
        self.assertEqual(400, response_put.status_code)
        
        

        
    
