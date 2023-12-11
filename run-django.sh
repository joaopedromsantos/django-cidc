#!/bin/sh

cd /code

python manage.py migrate --settings=proj.settings_prod
# python manage.py runserver 0.0.0.0:8000 --settings=proj.settings_prod
gunicorn proj.wsgi:application --env DJANGO_SETTINGS_MODULE=proj.settings_prod --limit-request-line 0 --timeout 600 -w 4 -b :8000
