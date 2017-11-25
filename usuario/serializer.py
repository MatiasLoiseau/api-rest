from rest_framework import serializers
from django.db import models
from usuario.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'user','password','email','cuenta')
