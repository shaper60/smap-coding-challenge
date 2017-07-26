# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

from ..models import User

class TestUrls(TestCase):

    def setUp(self):
        self.c = Client()
        self.user_id = 1
        User.objects.create(id=self.user_id,
                            area='hoge',
                            tariff='hoge')

    def test_summary(self):
        response = self.c.get('/summary/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.c.get('/detail/1')
        self.assertEqual(response.status_code, 200)