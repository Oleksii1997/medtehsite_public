import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your SECRET_KEY'

DEBUG = False

ALLOWED_HOSTS = ["your ALLOWED_HOSTS"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your db name',
        'USER': 'your user',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'stylesheet'),
)