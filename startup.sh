#!/usr/bin/env sh

docker-compose run vue npm i
docker-compose run app python /init_db.py

