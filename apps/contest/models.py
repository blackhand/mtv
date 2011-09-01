# -*- coding: utf-8 -*-

from django.db import models
from profile.models import Profile


class Product(models.Model):
    code = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class Option(models.Model):
    participant = models.ForeignKey(Profile)
    product = models.ForeignKey(Product)
    register_date = models.DateField()
    
    class Meta:
        verbose_name = 'opcion'
        verbose_name_plural = 'opciones'
        

class Draw(models.Model):
    DIARY = 1
    EXTRA = 2
    FINAL = 3
    TYPE_CHOICES = {
        'Diario': DIARY,
        'Extra': EXTRA, 
        'Final': FINAL,
    }
    play_date = models.DateField()
    winner = models.ForeignKey(Profile)


    class Meta:
        verbose_name = 'sorteo'
        verbose_name_plural = 'sorteos'
