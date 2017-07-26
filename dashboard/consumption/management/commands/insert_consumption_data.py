import csv
from glob import glob

from django.core.management.base import BaseCommand, CommandError

from consumption.models import User, Electricity


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('dashboard/data/user_data.csv', 'r') as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                info = {
                    'id': row[0],
                    'area': row[1],
                    'tariff': row[2],
                }

                try:
                    User.objects.get(pk=info['id'])
                except:
                    User(**info).save()

        for fn in glob('dashboard/data/consumption/*.csv'):
            user_id = fn.replace('dashboard/data/consumption/', '').replace('.csv', '')
            user = User.objects.get(pk=user_id)
            with open(fn, 'r') as f:
                rows = csv.reader(f)
                next(rows)
                for row in rows:
                    info = {
                        'user': user,
                        'datetime': row[0],
                        'consumption': row[1]
                    }
                    sample = {
                        'user': user.id,
                        'datetime': row[0],
                        'consumption': row[1]
                    }
                    print sample

                    if not Electricity.objects.filter(user=info['user'], datetime=info['datetime']):
                        print 'save!'
                        Electricity(**info).save()
                    else:
                        print 'pass!'
