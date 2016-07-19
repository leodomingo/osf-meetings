#!/bin/bash

rm ./db.sqlite3
rm ./submissions/migrations/0*
rm ./submissions/migrations/*.pyc
rm ./conferences/migrations/0*
rm ./conferences/migrations/*.pyc
rm ./approvals/migrations/0*
rm ./approvals/migrations/*.pyc
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
