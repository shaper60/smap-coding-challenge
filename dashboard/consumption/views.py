# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.db.models import Avg, Sum

from dashboard.utils.views import AdminViewMixin, paginate
from .models import User, Electricity
from .utils import ConsumptionChart


class SummaryView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': '#'}
    ]

    def get(self, request, *args, **kwargs):
        source = Electricity.objects.extra({'month': "strftime('%%Y%%m', datetime)"}).values('month').annotate(avg_consumption=Avg('consumption'), sum_consumption=Sum('consumption'))
        chart = ConsumptionChart(source=source, title='Summary')
        line_chart = chart.line_chart()
        user_list = User.objects.all()
        context = kwargs['context']
        context.update({
            'chart': line_chart,
            'user_list': user_list
        })
        return render(request, 'consumption/summary.html', context)


class DetailView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': reverse_lazy('consumption:summary')},
        {'name': 'Detail', 'url': '#'},
    ]

    def get(self, request, *args, **kwargs):
        source = Electricity.objects.filter(user=User.objects.get(pk=kwargs['user_id'])).extra({'month': "strftime('%%Y%%m', datetime)"}).values('month').annotate(avg_consumption=Avg('consumption'), sum_consumption=Sum('consumption'))
        chart = ConsumptionChart(source=source, title='Detail')
        line_chart = chart.line_chart()
        user = User.objects.get(pk=kwargs['user_id'])
        electricity_list = user.electricity_set.all()
        context = kwargs['context']
        context.update({
            'chart': line_chart,
            'user': user,
            'electricity_list': electricity_list
        })
        return render(request, 'consumption/detail.html', context)
