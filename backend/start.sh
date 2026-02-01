#!/usr/bin/env bash

python manage.py migrate
gunicorn backend.wsgi:application
