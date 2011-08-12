# -*- coding: utf-8 -*-

from django.db import models
from profile.models import Profile


class Product(models.Model):
    code = models.CharField(max_length=32)


class Options(models.Model):
    participant = models.ForeignKey(Profile)
    product = models.ForeignKey(Product)


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

