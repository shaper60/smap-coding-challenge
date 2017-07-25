# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel

from dashboard.utils.models import SoftDeleteBase


class User(TimeStampedModel, SoftDeleteBase):
    area = models.CharField(blank=False, max_length=3)
    tariff = models.CharField(blank=False, max_length=3)


class Electricity(TimeStampedModel, SoftDeleteBase):
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(blank=False)
    consumption = models.DecimalField(blank=False, max_digits=7, decimal_places=2)