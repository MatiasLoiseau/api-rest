from rest_framework.test import APITestCase
from django.core.management import call_command

class UsuarioTestCase(APITestCase):
    # Test module for Cuenta model

    def test_post_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario')
        usuario_data = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        response_post = self.client.post('/controlgastos/usuarios/', usuario_data, format='json')
        self.assertEqual(201, response_post.status_code)


    def test_delete_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario')
        call_command('loaddata', 'data_usr.json', app_label='usuario')
        response_delete = self.client.delete('/controlgastos/usuarios/1/', format='json')
        self.assertEqual(200, response_delete.status_code)

    def test_put_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario')
        call_command('loaddata', 'data_usr.json', app_label='usuario')
        usuario_data_modificada = {u'password': u'testpassword2', u'user2': u'testuser', u'cuenta': u'1',u'email': u'test@email.com'}
        response_put = self.client.put('/controlgastos/usuarios/1/', usuario_data_modificada, format='json')
        self.assertEqual(200, response_put.status_code)

    def test_bad_request_incorrect_type_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario')
        usuario_data_wrong = {u'password': u'testpassword', u'user': u'testuser', u'cuenta': u'SoyUnError', u'email': u'test@email.com'}
        response_post_wrong = self.client.post('/controlgastos/usuarios/', usuario_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

    def test_bad_request_field_required_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario')
        usuario_data_wrong = {u'user': u'testuser', u'cuenta': u'1', u'email': u'test@email.com'}
        response_post_wrong = self.client.post('/controlgastos/usuarios/', usuario_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)

    def test_bad_request_no_encuentra_recurso_usuario(self):
        call_command('loaddata', 'data_acc.json', app_label='usuario')
        usuario_data_wrong = {u'user': u'testuser', u'cuenta': u'99', u'email': u'test@email.com'}
        response_post_wrong = self.client.post('/controlgastos/usuarios/', usuario_data_wrong, format='json')
        self.assertEqual(400, response_post_wrong.status_code)
