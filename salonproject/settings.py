"""
Django settings for salonproject project.
Generated by 'django-admin startproject' using Django 3.2.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url
import django_heroku
import psycopg2
from pathlib import Path
#import cloudinary
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$(8+_2x(nyg_g_9exjv)xa!3qiy+1++x3zsgntzu$bkjy!!rfx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'salonapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salonproject.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR, 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = 'salonproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#HEROKU DATABASE 
#HEROKU_POSTGRESQL_MAROON_URL
DATABASE_URL='postgres://kcephsxhxheiob:d004979b53e452efde56c82adfcec829b73544fd151b38afa7f1bb49969dc6a3@ec2-3-226-134-153.compute-1.amazonaws.com:5432/d3saqmno8kra55'
DATABASES = {'default': dj_database_url.config(os.environ.get('DATABASE_URL'))
}

#LOCAL POSTGRES PSQL DATABASE 
'''
DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'salon_db',
        'USER' : 'postgres',
        'PASSWORD' : 'jeannette487547',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}'''

db_from_env = dj_database_url.config(conn_max_age=600)

#get data from heroku
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

'''
# STATIC FILES (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"
# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
 #   os.path.join(BASE_DIR, 'static_collections'),
#)
'''
# settings.py
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATICFILES_DIRS = (os.path.join(
    BASE_DIR, "salonapp", "static"),)
STATIC_ROOT = os.path.join(
    os.path.dirname(BASE_DIR), "deployment", "collected_static")
MEDIA_ROOT = os.path.join(
    os.path.dirname(BASE_DIR), "deployment", "media")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    #'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = 'deployment/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#EMAIL 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "madeleinesalondecoiffure@gmail.com"
EMAIL_HOST_PASSWORD = 'Moselle1'
EMAIL_PORT = '587'

django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

#cloudinary://784459254455196:888jgqkxGPBr5HPIUsNPBerqnQ8@madeleinesalondecoiffure
#cloudinary.config( 
 # cloud_name = "madeleinesalondecoiffure", 
  #api_key = "784459254455196", 
  #api_secret = "888jgqkxGPBr5HPIUsNPBerqnQ8" 
#)