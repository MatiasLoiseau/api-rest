from django.db import models

#Se crea el modelo de cuenta

class Cuenta(models.Model):
    nombre = models.CharField(max_length=200)
