from rest_framework import serializers
from cuentas.models import Cuenta

class CuentaSerializer(serializers.Serializer):
    nombreCuenta = serializers.CharField(required=False, allow_blank=True, max_length=30)
    def create(self, validated_data):
        """
        Create and return a new `Cuenta` instance, given the validated data.
        """
        return Cuenta.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Cuenta` instance, given the validated data.
        """
        instance.nombreCuenta = validated_data.get('nombreCuenta', instance.nombreCuenta)
        instance.save()
        return instance