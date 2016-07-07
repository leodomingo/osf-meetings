#!/bin/bash


rm -rf db.sqlite
rm api/migrations/0*
./manage.py makemigrations
./manage.py migrate
./manage.py loadtestdata conferences.Conference:10000
./manage.py runserver
