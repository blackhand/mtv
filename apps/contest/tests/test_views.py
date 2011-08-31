# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from datetime import date

from contest.models import Draw

class ViewsTestCase(TestCase):

    fixtures = ['initial_data.yaml']

    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))

    def post(self, url_name, *args, **kwargs):
        data = kwargs.pop("data", None)
        return self.client.post(reverse(url_name, args=args, kwargs=kwargs), data)

    def test_get_winners(self):
        """
        all winners
        """
        resp = self.get('show_winners')
        # redirect
        self.assertEqual(resp.status_code, 302)
