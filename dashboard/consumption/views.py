# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.db.models import Avg, Sum

from chartit import DataPool, Chart

from dashboard.utils.views import AdminViewMixin, paginate
from .models import User, Electricity


class SummaryView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': '#'}
    ]

    def get(self, request, *args, **kwargs):
        summarydata = DataPool(
            series=[{
                'options': {
                    'source': Electricity.objects.extra({'month': "strftime('%%Y%%m', datetime)"}).values('month').annotate(avg_consumption=Avg('consumption'), sum_consumption=Sum('consumption'))
                },
                'terms': [
                    'month',
                    'avg_consumption',
                    'sum_consumption'
                ]
            }]

        )

        cht = Chart(
            datasource=summarydata,
            series_options=[{
                'options': {
                    'type': 'line',
                    'stacking': False
                },
                'terms': {
                    'month' : [
                        'avg_consumption',
                        'sum_consumption'
                    ]
                }
            }],
            chart_options={
                'title': {
                    'text': 'Summary　Chart'
                },
                'xAxis': {
                    'title': {
                        'text': 'month'
                    }
                }
            }
        )

        user_list = User.objects.all()
        context = kwargs['context']
        context.update({
            'summarychart': cht,
            'user_list': user_list
        })
        return render(request, 'consumption/summary.html', context)


class DetailView(AdminViewMixin, View):
    breadcrumbs = [
        {'name': 'Summary', 'url': reverse_lazy('consumption:summary')},
        {'name': 'Detail', 'url': '#'},
    ]

    def get(self, request, *args, **kwargs):
        summarydata = DataPool(
            series=[{
                'options': {
                    'source': Electricity.objects.filter(user=User.objects.get(pk=kwargs['user_id'])).extra({'month': "strftime('%%Y%%m', datetime)"}).values('month').annotate(avg_consumption=Avg('consumption'), sum_consumption=Sum('consumption'))
                },
                'terms': [
                    'month',
                    'avg_consumption',
                    'sum_consumption'
                ]
            }]

        )

        cht = Chart(
            datasource=summarydata,
            series_options=[{
                'options': {
                    'type': 'line',
                    'stacking': False
                },
                'terms': {
                    'month' : [
                        'avg_consumption',
                        'sum_consumption'
                    ]
                }
            }],
            chart_options={
                'title': {
                    'text': 'Summary　Chart'
                },
                'xAxis': {
                    'title': {
                        'text': 'month'
                    }
                }
            }
        )
        user = User.objects.get(pk=kwargs['user_id'])
        electricity_list = user.electricity_set.all()
        context = kwargs['context']
        context.update({
            'summarychart': cht,
            'user': user,
            'electricity_list': electricity_list
        })
        return render(request, 'consumption/detail.html', context)
