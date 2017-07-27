# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel

from dashboard.utils.models import SoftDeleteBase


class User(TimeStampedModel, SoftDeleteBase):
    area = models.CharField(blank=False, max_length=3)
    tariff = models.CharField(blank=False, max_length=3)

    def __str__(self):
        return "id={0}".format(self.id)


class Electricity(TimeStampedModel, SoftDeleteBase):
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(blank=False)
    consumption = models.DecimalField(blank=False, max_digits=7, decimal_places=2)

    def __str__(self):
        return "id={0}, user_id={1}".format(self.id, self.user.id)