# -*- coding: utf-8 -*-

from django.db import models
from django.core.mail import send_mail
from django.http import HttpResponse
from smtplib import SMTPException


class Contact(models.Model):
    """
    Generic Contact for Sancela - Nosotras - MTV registered users
    """
    first_name   = models.CharField('nombres', max_length=64)
    second_name  = models.CharField('apellidos', max_length=64)
    email        = models.EmailField('email')
    comment      = models.TextField('comentario')
    reply        = models.TextField('respuesta',blank=True)
    responded    = models.BooleanField('respondido',editable=False,default=True)
    new          = models.BooleanField('nuevo',editable=False,default=True)
    
    objects = models.Manager()

    class Meta:
        verbose_name = 'comentario enviado'
        verbose_name_plural = 'comentarios enviados (todos)'
    
    def __unicode__(self):
        return u'%s %s %s'% ('Comentario de ', self.first_name, self.second_name, )

    def get_subject(self):
        """
        return subject
        """
        return u'%s %s' % (self.first_name, self.second_name)

    def save(self, *args, **kwargs):
        """
        we overload here save to send mail
        """
        if self.new:
            try:
                send_mail(self.get_subject, self.comment, self.email, ['themiseck.rock@gmail.com'])
            except SMTPException:
                return HttpResponse('Error al enviar mail')
        else:
            if not self.responded:
                try:
                    send_mail('Nosotras', self.reply, 'themiseck.rock@gmail.com', [self.email])
                except SMTPException:
                    return HttpResponse('Error al enviar mail')
            self.responded = False
        super(Contact, self).save(*args, **kwargs)
        self.new = False


class PendingContact(Contact):
    class Meta:
        proxy = True
        verbose_name = 'comentario pendiente de respuesta'
        verbose_name_plural = 'comentarios pendientes de respuesta'


class RespondedContact(Contact):
    class Meta:
        proxy = True
        verbose_name = 'comentario respondido'
        verbose_name_plural = 'comentarios respondidos'
