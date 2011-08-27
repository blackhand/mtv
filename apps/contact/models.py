# -*- coding: utf-8 -*-

from django.db import models


class Contact(models.Model):
    """
    Generic Contact for Sancela - Nosotras - MTV registered users
    """
    first_name   = models.CharField('nombres', max_length=64)
    second_name  = models.CharField('apellidos', max_length=64)
    mail         = models.EmailField('email')
    comment      = models.TextField()
    reply        = models.TextField(blank=True)
    responded    = models.BooleandField(default=False)

    def getSubject():
		"""
        return subject
        """
        return u'%s %s' % (self.first_name, self.second_name)

    def save(self, *args, **kwargs)
        """
        we overload here save to send mail
        """
        if not responded:
            try:
                send_mail(self.getSubject, self.comment, self.mail, ['mcumpa@tribal.com'])
            except SMTPException:
                return HttpResponse('Error al enviar mail')
        else
            try:
                send_mail('Nosotroas', self.reply, 'mcumpa@tribal.com', [self.mail])
            except SMTPException:
                return HttpResponse('Error al enviar mail')
        self.responded = True
        super(Contact, self).save(*args, **kwargs)
