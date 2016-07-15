#!/bin/bash

rm ./db.sqlite3
cd ./submissions/migrations
rm 0*
cd ../../
cd ./conferences/migrations
rm 0*
cd ../../
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
