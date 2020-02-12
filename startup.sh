#!/usr/bin/env sh

docker-compose run app python /init_db.py
docker-compose run vue npm i

