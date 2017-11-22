from rest_framework import serializers
from usuarios.models import Usuario
from cuentas.serializers import CuentaSerializer

class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=True, max_length=30)
    password = serializers.CharField(required=False, allow_blank=True, max_length=30)
    email = serializers.CharField(required=False, allow_blank=True, max_length=30)
    cuentas = CuentaSerializer()

    def create(self, validated_data):
        """
        Crea y devuelve una nueva instancia de `Usuario`.
        """
        return Usuario.objects.create(**validated_data)

    '''def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''