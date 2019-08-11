#!/usr/bin/env bash

#sleep 86000
python manage.py migrate
#python manage.py runserver

gunicorn --workers 5 --bind 0.0.0.0:9001 main.wsgi:application
