Prerequeisites:
- python3
- pip
- virtualenv
- postgresql

Make a python3 virtualenv, start it, and install python packages
`$ virtualenv -p python3 venv`
`$ . venv/bin/activate`
`$ pip install -r requirements.txt`

Setup postgressql
$ sudo -u postgres psql
`postgres=# CREATE DATABASE eventplanner;`
`postgres=# CREATE USER event WITH PASSWORD 'password';`
`postgres=# ALTER ROLE event SET client_encoding TO 'utf8';`
`postgres=# ALTER ROLE event SET default_transaction_isolation TO 'read committed';`
`postgres=# ALTER ROLE event SET timezone TO 'UTC';`
`postgres=# GRANT ALL PRIVILEGES ON DATABASE eventplanner TO event;`
`postgres=# \q`

Setup local.env
`$ cp event_planner_api/local_env_template.txt event_planner_api/local.env`
Fill in local.env settings
export DB_NAME='eventplanner'
export DB_USERNAME='event'
export DB_PASSWORD='password'
`$ . event_planner_api/local.env`
