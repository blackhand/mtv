# -*- coding: utf-8 -*-

from django.db import models
from profile.models import Profile


class Option(models.Model):
    participant = models.ForeignKey(Profile)
    product_code = models.CharField('codigo', max_length=32)
    register_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'opcion'
        verbose_name_plural = 'opciones'
        

class Draw(models.Model):
    play_date = models.DateField()
    winner = models.ForeignKey(Profile)


    class Meta:
        verbose_name = 'sorteo'
        verbose_name_plural = 'sorteos'
