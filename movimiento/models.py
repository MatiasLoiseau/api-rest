from django.db import models
from categoria.models import Categoria
from usuario.models import Usuario
#Se crea el modelo de Movimiento


class Movimiento(models.Model):
    monto = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
