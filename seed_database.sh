#!/bin/bash

rm db.sqlite3
rm -rf ./raterapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations raterapi
python3 manage.py migrate raterapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

python manage.py loaddata categories.json
python manage.py loaddata games.json
python manage.py loaddata game_images.json
python manage.py loaddata reviews.json
python manage.py loaddata game_categories.json
