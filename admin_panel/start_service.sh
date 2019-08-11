#!/usr/bin/env bash

#sleep 86000
python manage.py migrate
python manage.py collectstatic
#python manage.py runserver

gunicorn --workers 1 --timeout 400 --bind 0.0.0.0:9001 main.wsgi:application
