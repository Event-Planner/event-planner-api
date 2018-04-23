from os import getenv
import sys

IS_UNIT_TEST = False
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    IS_UNIT_TEST = True

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

# Passwords
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if IS_UNIT_TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'testing/event_planner_api.testdb.sqlite',
            'TEST': {
                'NAME': 'testing/event_planner_api.testdb.sqlite',
            }
        }
    }
    AUTH_PASSWORD_VALIDATORS = []
    PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
    MIDDLEWARE = []
    SERVER_RUN_LEVEL = False
else:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': DB_NAME,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }

# Authenitcation env vars
TOKEN_TIMEOUT_DAYS = getenv('TOKEN_TIMEOUT_DAYS', 7)
