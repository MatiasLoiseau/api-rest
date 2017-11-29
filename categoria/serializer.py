from rest_framework import serializers
from django.db import models
from categoria.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre','cuenta')