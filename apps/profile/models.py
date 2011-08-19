# -*- coding: utf-8 -*-

from django.db import models
from ubigeo.models import Ubigeo


class Profile(models.Model):
    """
    Generic Profile for Sancela - Nosotras - MTV registered users
    """
    first_name = models.CharField('nombres', max_length=64)
    last_name = models.CharField('apellidos', max_length=64)
    email = models.EmailField('email', unique=True)
    birth_date = models.DateField('fecha de nacimiento')
    ubigeo = models.ForeignKey(Ubigeo, verbose_name='ubigeo')
    address = models.CharField('direccion', max_length=64)
    home_phone = models.CharField('telefono fijo', max_length=9)
    mobile_phone = models.CharField('movil', max_length=9)
    document_code = models.CharField('DNI', max_length=8)
    
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

