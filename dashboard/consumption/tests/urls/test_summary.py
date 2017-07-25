# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

class TestSummary(TestCase):
    def test_summary(self):
        c = Client()
        response = c.get('/summary/')
        self.assertEqual(response.status_code, 200)