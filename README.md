# Readme

## Build

`docker-compose build` to build docker images

## DB init

After cloning run this command to set up db and node_modules

```shell script
sh startup.sh
```

## Run

`docker-compose up` to serve app

## Tests

Run tests with pytest in environment with `src/requirements.txt` installed

1. `cd py`
2. `pip -r src/requirements.txt`
3. `pytest tests/test_count.py`

