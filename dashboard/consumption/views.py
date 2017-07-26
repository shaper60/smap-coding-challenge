# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy

from dashboard.utils.views import AdminViewMixin, paginate
from .models import User, Electricity


class SummaryView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': '#'}
    ]

    def get(self, request, *args, **kwargs):
        user_list = User.objects.all()
        context = kwargs['context']
        context.update({
            'user_list': user_list
        })
        return render(request, 'consumption/summary.html', context)


class DetailView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': reverse_lazy('consumption:summary')},
        {'name': 'Detail', 'url': '#'},
    ]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        electricity_list = user.electricity_set.all()
        print electricity_list
        context = kwargs['context']
        context.update({
            'user': user,
            'electricity_list': electricity_list
        })
        return render(request, 'consumption/detail.html', context)
