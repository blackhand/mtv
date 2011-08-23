# -*- coding: utf-8 -*-

from django.utils import unittest
from django.contrib.auth.models import User
from datetime import date

from ubigeo.models import Ubigeo
from models import Profile

class ProfileTestCase(unittest.TestCase):

    fixtures = ['initial_data.yaml']

    # Model tests
    def test_profile_create_user(self):
        # Marcapata, Cusco, Cusco
        ubigeo = Ubigeo.objects.get(id=81209)
        p=Profile.objects.create(
                first_name = 'Bergamino',
                first_surname = 'Suarez',
                second_surname = 'Alcantara',
                email = 'usuario@mailinator.com',
                birth_date = date(1999, 10, 10),
                ubigeo = ubigeo,
                address = 'XXXXXXXXXXXXXXXXX',
                home_phone = '4444444',
                mobile_phone = '999999999',
                document_code = '40404040',
                )
        self.assertEqual(p.user.username, 'usuario_mailinator_com')

    # View Tests

