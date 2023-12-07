from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# False if not in os.environ because of casting above
DJANGO_ENV = os.getenv('DJANGO_ENV')


if DJANGO_ENV == "development":
   DEBUG = True
else:
   DEBUG = False


# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = os.getenv('SECRET_KEY',default='defaultsecret')


ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS',default='*')]




# Database


if DJANGO_ENV == 'development':
   DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
   }
else:
   DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'PGDATABASE': os.getenv('PGDATABASE'),
       'PGUSER': os.getenv('PGUSER'),
       'PGPASSWORD': os.getenv('PGPASSWORD'),
       'PGHOST': os.getenv('PGHOST'),
       'PGPORT': '5432',
       'OPTIONS': {
           'sslmode': 'require',
       },
   }
}






