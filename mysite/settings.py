"""
Django settings for mysite project.
Generated by 'django-admin startproject' using Django 2.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = [('Nate','Nate.spilman@gmail.com')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['142.93.245.126','localhost:8000','localhost','natespilman.tech','pioneer-django.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',

    #myApps
    'subscriptions',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },  
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

ENV_PATH = os.path.abspath(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(ENV_PATH, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')
MEDIA_URL = '/media/'

### SHHHHHHH
import environ
import json

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = os.environ.get('SECRET_KEY',env('SECRET_KEY'))
DEBUG = json.loads(os.environ.get('DEBUG',env('DEBUG')).lower())

EMAIL_HOST = 'smtp.gmail.com'  # since you are using a gmail account
EMAIL_PORT = 587  # Gmail SMTP port for TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER",env('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD",env('EMAIL_HOST_PASSWORD'))
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS",env('CORS_ALLOWED_ORIGINS')).split(',')

### Google Sheets settings
GSHEET_CONFIG = os.environ.get("GSHEET_CONFIG",env("GSHEET_CONFIG"))
try:
    import django_heroku
    django_heroku.settings(locals())
except:
    print('django_heroku not installed')