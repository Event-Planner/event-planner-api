from os import getenv

# Django specific env vars
SECRET_KEY = getenv('SECRET_KEY')
SERVER_RUN_LEVEL = getenv('SERVER_RUN_LEVEL', True)
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', ['127.0.0.1', 'localhost', '0.0.0.0'])
DJANGO_STATIC_URL = getenv('DJANGO_STATIC_URL', '/static/')

# Database env vars
DB_ENGINE = getenv('DB_ENGINE', 'django.db.backends.postgresql_psycopg2')
DB_NAME = getenv('DB_NAME')
DB_USERNAME = getenv('DB_USERNAME')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST', 'localhost')
DB_PORT = getenv('DB_PORT', '')

# Authenitcation env vars
TOKEN_TIMEOUT_DAYS = getenv('TOKEN_TIMEOUT_DAYS', 7)
