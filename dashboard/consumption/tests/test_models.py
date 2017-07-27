# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.test import TestCase

from ..models import User, Electricity


class TestModels(TestCase):

    def setUp(self):
        self.datetime = datetime.now()
        self.user = User(area='aaa',
                         tariff='aaa')
        self.user.save()

    def test_user_creation(self):
        user_db = User.objects.get(area='aaa')
        self.assertEqual(self.user, user_db)

    def test_electricity_creation(self):
        electricity = Electricity(user=self.user, 
                                  datetime=self.datetime,
                                  consumption=200.10)
        electricity.save()
        electricity_db = Electricity.objects.get(datetime=self.datetime)
        self.assertEqual(electricity, electricity_db)
