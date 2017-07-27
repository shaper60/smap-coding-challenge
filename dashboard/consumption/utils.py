from chartit import DataPool, Chart


class ConsumptionChart(object):
    def __init__(self, source, title):
        self.source = source
        self.title = title
    
    def line_chart(self):
        data = self._data()
        return self._chart(data, 'line')

    def pivot_chart(self):
        data = self._data()
        return self._chart(data, 'column')

    def _data(self):
        return DataPool(
            series=[{
                'options': {
                    'source': self.source
                },
                'terms': [
                    'month',
                    'avg_consumption',
                    'sum_consumption'
                ]
            }]

        )

    def _chart(self, data, chart_type='line'):
        chart = Chart(
            datasource=data,
            series_options=[{
                'options': {
                    'type': chart_type,
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
                    'text': '{0} Chart'.format(self.title)
                },
                'xAxis': {
                    'title': {
                        'text': 'month'
                    }
                }
            }
        )
        return chart
