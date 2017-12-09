from rest_framework import serializers
from django.db import models
from movimiento.models import Movimiento


class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ('id','fecha','user','monto','categoria','descripcion')
