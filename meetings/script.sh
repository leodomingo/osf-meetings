#!/bin/bash

rm api/migrations/0*
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
