# -*- coding: utf-8 -*-

from django.test import TestCase

from ubigeo.models import Ubigeo
from profile.models import Profile

from datetime import date

class ModelsTestCase(TestCase):

    def setUp(self):
        pass

    def test_profile_create_user(self):
        ubigeo = Ubigeo.objects.get(id=81209)
        self.profile=Profile.objects.create(
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
        self.assertEqual(self.profile.user.username, 'usuario_mailinator_com')


