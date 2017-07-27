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
        user_list = paginate(request, User.objects.all(), 10)

        source = Electricity.objects \
                     .extra({'month': "strftime('%%Y%%m', datetime)"}) \
                     .values('month') \
                     .annotate(avg_consumption=Avg('consumption'),
                               sum_consumption=Sum('consumption'))
        chart = ConsumptionChart(source=source, title='Summary')
        line_chart = chart.line_chart()
        
        context = kwargs['context']
        context.update({
            'user_list': user_list,
            'chart': line_chart,
        })
        return render(request, 'consumption/summary.html', context)


class DetailView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': reverse_lazy('consumption:summary')},
        {'name': 'Detail', 'url': '#'},
    ]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])

        electricity_list = paginate(request, user.electricity_set.all(), 10)

        source = Electricity.objects \
                     .filter(user=user)  \
                     .extra({'month': "strftime('%%Y%%m', datetime)"}) \
                     .values('month') \
                     .annotate(avg_consumption=Avg('consumption'),
                               sum_consumption=Sum('consumption'))
        cht = ConsumptionChart(source=source, title='Detail')
        line_chart = cht.line_chart()

        context = kwargs['context']
        context.update({
            'user': user,
            'electricity_list': electricity_list,
            'chart': line_chart,
        })
        return render(request, 'consumption/detail.html', context)
