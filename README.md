# Flask Example Project

## Quick Start

### First Steps

```sh
$ virtualenv --python=/usr/bin/python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

This service requires running `PostgreSQL` and `RabbitMQ` instances.

### Set up Migrations

```sh
$ alembic upgrade head
```

### Run

Run each in a different terminal window

```sh
# worker process
$ python worker.py

# the app
$ python app.py
```

For running with uWSGI use

```bash
uwsgi --socket 0.0.0.0:8000 --protocol=http -w app
```
