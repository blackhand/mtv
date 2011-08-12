# -*- coding: utf-8 -*-

from django.db import models
from ubigeo.models import Ubigeo


class Profile(models.Model):
    """
    Generic Profile for Sancela - Nosotras - MTV registered users
    """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    ubigeo = models.ForeignKey(Ubigeo)
    address = models.CharField(max_length=64)
    home_phone = models.CharField(max_length=9)
    mobile_phone = models.CharField(max_length=9)
    document_code = models.CharField(max_length=8)
    
    class Meta:
        verbose_name = 'Usuaria Registrado'
        verbose_name_plural = 'Usuarias Registrado'
    
    def __unicode__(self):
        return u'%s %s'% (self.first_name, self.last_name)
    
    def save(self, force_insert=False, force_update=False):
        super(Profile, self).save(force_insert=force_insert, force_update=force_update)
    
    @models.permalink
    def get_absolute_url(self):
        return ('profile')

