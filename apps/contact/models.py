# -*- coding: utf-8 -*-

from django.db import models
from django.core.mail import send_mail
from smtplib import SMTPException

class Contact(models.Model):
    """
    Generic Contact for Sancela - Nosotras - MTV registered users
    """
    first_name   = models.CharField('nombres', max_length=64)
    second_name  = models.CharField('apellidos', max_length=64)
    email         = models.EmailField('email')
    comment      = models.TextField('comentario')
    reply        = models.TextField('respuesta',blank=True)
    responded    = models.BooleanField('respondido',editable=False,default=False)

    class Meta:
        verbose_name = 'Comentario Enviado'
        verbose_name_plural = 'Comentarios Enviados'
    
    def __unicode__(self):
        return u'%s %s %s'% (self.first_name, self.first_surname, self.second_surname)

    def getSubject():
        """
        return subject
        """
        return u'%s %s' % (self.first_name, self.second_name)

    def save(self, *args, **kwargs):
        """
        we overload here save to send mail
        """
        if not self.responded:
            try:
                send_mail(self.getSubject, self.comment, self.email, ['themiseck.rock@gmail.com'])
            except SMTPException:
                return HttpResponse('Error al enviar mail')
        else:
            try:
                send_mail('Nosotroas', self.reply, 'themiseck.rock@gmail.com', [self.email])
            except SMTPException:
                return HttpResponse('Error al enviar mail')
        self.responded = True
        super(Contact, self).save(*args, **kwargs)
