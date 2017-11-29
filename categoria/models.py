# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from cuenta.models import Cuenta

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    #falta lista de movimientos asignados a esta categoria
