# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from ubigeo.models import Ubigeo


class Profile(models.Model):
    """
    Generic Profile for Sancela - Nosotras - MTV registered users
    """
    user            = models.OneToOneField('auth.User', editable=False)
    first_name      = models.CharField('nombres', max_length=64)
    first_surname   = models.CharField('apellido materno', max_length=64)
    second_surname  = models.CharField('apellido paterno', max_length=64)
    email           = models.EmailField('email', unique=True)
    birth_date      = models.DateField('fecha de nacimiento')
    ubigeo          = models.ForeignKey(Ubigeo, verbose_name='ubigeo')
    address         = models.CharField('direccion', max_length=64)
    home_phone      = models.CharField('telefono fijo', max_length=9)
    mobile_phone    = models.CharField('movil', max_length=9)
    document_code   = models.CharField('DNI', max_length=8)
    is_participant  = models.BooleanField('Participa', default=False, editable=False)

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'Usuaria Registrado'
        verbose_name_plural = 'Usuarias Registradas'
    
    def __unicode__(self):
        return u'%s %s %s'% (self.first_name, self.first_surname, self.second_surname)

    def generate_username(self):
        return self.email.replace('@','_').replace('.','_')

    
    def save(self, *args, **kwargs):
        """
        we overload here save to maintain sincronized User with Profile model
        first_name, last_name and email fields Profile fields -> User fields
        """
        try:
            user = self.user
        except User.DoesNotExist:
            user = User(username=self.generate_username(), email=self.email)
            user.set_unusable_password()
            user.save()
            self.user = user

        user.first_name = self.first_name
        user.last_name = u'%s %s' % (self.first_surname, self.second_surname)
        user.email = self.email
        user.save()
        super(Profile, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('profile')

