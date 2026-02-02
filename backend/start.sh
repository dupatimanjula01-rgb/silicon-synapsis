#!/usr/bin/env bash

echo "RUNNING MIGRATIONS"
python manage.py migrate

echo "CREATING ADMIN"
python manage.py create_admin

echo "STARTING SERVER"
gunicorn backend.wsgi:application
