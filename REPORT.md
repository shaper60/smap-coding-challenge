## Requirement
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install --requirement requirements.txt
$ cd dashboard
```

## Usage
```
# Start the server
$ python manage.py runserver
```

## Install
```
$ git clone git@github.com:shaper60/smap-coding-challenge.git
```

## Initial data
```
$ python manage.py insert_csv_data
```

## Open question
- How to save the User data and the Consumption data. CSV upload or something else?
- Consumption's max digits and the number of decimal places.
- User area and tariff's max character length.
- How to customize the data type of chart.
