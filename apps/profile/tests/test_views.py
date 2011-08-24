# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from datetime import date


class ViewsTestCase(TestCase):

    fixtures = ['initial_data.yaml']

    EMAIL = 'ana@mailinator.com'
    BIRTH_DATE = date(1999, 9, 9)

    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))

    def post(self, url_name, *args, **kwargs):
        data = kwargs.pop("data", None)
        return self.client.post(reverse(url_name, args=args, kwargs=kwargs), data)

    def test_get_login(self):
        """
        basic view login page
        """
        resp = self.get('profile_login')
        self.assertEqual(resp.status_code, 200)

    def test_post_login(self):
        """
        basic login attempt
        """
        resp = self.post('profile_login', data = {
            'email': ViewsTestCase.EMAIL,
            'birth_date': ViewsTestCase.BIRTH_DATE,
            })
        self.assertEqual(resp.status_code, 200)

    def test_login_new(self):
        """
        login attempt with and unregistered user
        must go to register profile view
        """
        self.test_post_login()

    def test_login_existing(self):
        """
        """
        self.test_post_login()
