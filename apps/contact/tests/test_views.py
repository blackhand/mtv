# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
##from datetime import date

from contact.models import Contact

class ViewsTestCase(TestCase):

    USER_EMAIL = {
        'first_name': 'Mariana',
        'second_name': 'Ramirez Vargas',
        'email': 'themiseck.rock@gmail.com',
        'comment': 'Correo de mierda llega!!!!!!!!',
        }

    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))

    def post(self, url_name, *args, **kwargs):
        data = kwargs.pop("data", None)
        return self.client.post(reverse(url_name, args=args, kwargs=kwargs), data)

    def test_send_comment(self):
        resp = self.post('contact_send',data = self.USER_EMAIL)
        self.assertEqual(resp.status_code, 302)
