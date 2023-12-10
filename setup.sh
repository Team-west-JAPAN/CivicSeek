#!/bin/bash

python3 -m venv venv # create virtual environment for python

. ./venv/bin/activate # activate venv

pip install -r requirements.txt # install required packages

python3 regenerateSecretKey.py # regenerate secret key

python3 ./manage.py migrate # migrate DB

python3 manage.py loaddate ./sample_db.json # add Contents of the database

python3 manage.py runserver # activate server