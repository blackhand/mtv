# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from datetime import date


class ViewsTestCase(TestCase):

    fixtures = ['initial_data.yaml']

    TEST_EMAIL = 'ana@mailinator.com'
    TEST_BIRTHDATE = date(1999, 9, 9)

    def test_get_login(self):
        resp = self.client.get(reverse('profile_login'))
        self.assertEqual(resp.status_code, 200)

    def test_post_login(self):
        resp = self.client.post(reverse('profile_login'), {
            'email': ViewsTestCase.TEST_EMAIL,
            'birth_date': ViewsTestCase.TEST_BIRTHDATE,
            })
        self.assertEqual(resp.status_code, 200)

    def test_login_new(self):
        self.test_post_login()
