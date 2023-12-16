# This Python Basic

## getting start

```sh
$ docker-compose build
$ docker-compose up -d
```

## env

- `cp .env_sample .env`
- your application path setting

## how to

```sh
# instal python libs
$ docker exec -it python3 pip list
# in container
$ docker exec -it python3 /bin/bash
# code execution
$ docker exec -it python3 python main.py
```
