from cuentas.models import Cuenta
from cuentas.serializers import CuentaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

cuenta = Cuenta(nombreCuenta='nombrecualquiera')
cuenta.save()

serializer = CuentaSerializer(cuenta)
serializer.data

content = JSONRenderer().render(serializer.data)
content