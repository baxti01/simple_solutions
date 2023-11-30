#!/bin/bash


./wait-for-it.sh -t 120 db:5432 -- echo "postgres is up"

python manage.py makemigrations
python manage.py migrate

# Это пользовательская команда
python manage.py initsuperuser

python manage.py runserver 0.0.0.0:8000
