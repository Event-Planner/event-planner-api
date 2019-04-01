# event-planner-api

# Installation

## Prerequisites:
- python3 (macOS)
- python3.7 (Linux)
- pip
- virtualenv
- postgresql

## Make a python3 virtualenv, start it, and install python packages
1. `$ make setup`

## Setup postgressql
1. `$ sudo -u postgres psql`
2. `postgres=# CREATE DATABASE eventplanner;`
3. `postgres=# CREATE USER event WITH PASSWORD 'password';`
4. `postgres=# ALTER ROLE event SET client_encoding TO 'utf8';`
5. `postgres=# ALTER ROLE event SET default_transaction_isolation TO 'read committed';`
6. `postgres=# ALTER ROLE event SET timezone TO 'UTC';`
7. `postgres=# GRANT ALL PRIVILEGES ON DATABASE eventplanner TO event;`
8. `postgres=# \q`

## Setup local.env
1. `$ cp local_env_template.txt local.env`
2. Fill in local.env settings
```bash
export DB_NAME='eventplanner'
export DB_USERNAME='event'
export DB_PASSWORD='password'
```
3. `$ . local.env` or `$ source local.env`
