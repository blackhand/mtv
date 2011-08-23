# -*- coding: utf-8 -*-
"""
models for ubigeo utils
"""

from django.db import models


class Ubigeo(models.Model):
    name = models.CharField('nombre', max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True)

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'Ubigeo'
        verbose_name_plural = 'Ubigeos'
