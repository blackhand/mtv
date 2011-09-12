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
    document_code   = models.CharField('DNI', max_length=8, unique=True)
    is_participant  = models.BooleanField('participa', default=False, editable=False)
    is_winner       = models.BooleanField('ganadora', default=False, editable=False)

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
    

class Registered(Profile):
    " Proxy model for registered users"
    
    class Meta:
        proxy = True
        verbose_name = 'Usuaria Registrada'
        verbose_name_plural = 'Usuarias Registradas'


class ParticipantManager(models.Manager):
    def get_query_set(self):
        return super(ParticipantManager, self).get_query_set().filter(is_participant=True)


class Participant(Profile):
    objects = ParticipantManager()
    class Meta:
        proxy = True
        verbose_name = 'Participante Registrada'
        verbose_name_plural = 'Participantes Registradas'


class WinnerManager(models.Manager):
    def get_query_set(self):
        return super(WinnerManager, self).get_query_set().filter(is_winner=True)


class Winner(Profile):
    objects = WinnerManager()
    class Meta:
        proxy = True
        verbose_name = 'Ganadoras'
        verbose_name_plural = 'Ganadoras'


class TblUsuarios(models.Model):
    pk_usuario = models.IntegerField(primary_key=True)
    txt_nombre = models.CharField(max_length=300, blank=True)
    txt_apellido_paterno = models.CharField(max_length=300, blank=True)
    txt_apellido_materno = models.CharField(max_length=300, blank=True)
    txt_correo = models.CharField(max_length=300, blank=True)
    txt_tipo_doc = models.CharField(max_length=90, blank=True)
    txt_num_doc = models.CharField(unique=True, max_length=24, blank=True)
    date_nacimiento = models.DateField(null=True, blank=True)
    txt_telefono = models.CharField(max_length=45, blank=True)
    txt_celular = models.CharField(max_length=27, blank=True)
    int_operador = models.CharField(max_length=3, blank=True)
    txt_direccion = models.CharField(max_length=300, blank=True)
    date_registro = models.DateTimeField(null=True, blank=True)
    txt_departamento = models.CharField(max_length=240, blank=True)
    txt_provincia = models.CharField(max_length=240, blank=True)
    txt_distrito = models.CharField(max_length=450, blank=True)

    class Meta:
        db_table = u'tbl_usuarios'
        managed = False
