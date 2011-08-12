# -*- coding: utf-8 -*-
"""
models for ubigeo utils
"""

from django.db import models


class Ubigeo(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self")
    
    class Meta:
        verbose_name = 'Ubigeo'
        verbose_name_plural = 'Ubigeos'


