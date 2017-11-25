from django.db import models
from cuenta.models import Cuenta
#Se crea el modelo de usuario


class Usuario(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE) #Verificar relaciones y si hay que usar cascadeo
