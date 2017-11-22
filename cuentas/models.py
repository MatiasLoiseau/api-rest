# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles

#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Cuenta(models.Model):
    nombreCuenta = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.nombreCuenta

    class Meta:
        ordering = ('nombreCuenta',)

