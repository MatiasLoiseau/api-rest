# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cuentas.models import Cuenta

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    #cuentas = models.ManyToManyField(Cuenta,on_delete=models.CASCADE) --> NO anda el on_delete:
    """ERROR:  	File "/home/matias/api-rest/usuarios/models.py", line 13, in Usuario
    				cuentas = models.ManyToManyField(Cuenta,on_delete=models.CASCADE) #relaciono con la cuentas, pueden tener mas de una?
  				File "/home/matias/api-rest/env/local/lib/python2.7/site-packages/django/db/models/fields/related.py", line 1185, in __init__
    				super(ManyToManyField, self).__init__(**kwargs)
				TypeError: __init__() got an unexpected keyword argument 'on_delete'"""
    cuentas = models.ManyToManyField(Cuenta) #relaciono con la cuentas, pueden tener mas de una?
    def __str__(self):              # __unicode__ on Python 2
        return self.username

    class Meta:
        ordering = ('username',)
