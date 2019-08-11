#!/usr/bin/env bash

python admin_panel/manage.py migrate

gunicorn --workers 1 --bind 0.0.0.0:9001 admin_panel.admin_panel.wsgi:application
