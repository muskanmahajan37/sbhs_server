"""
Django settings for sbhs_server project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sbhs_server.credentials as credentials

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/sudo cat /var/log/auth.log | grep "session opened for user root"howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = credentials.PROJECT_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '10.119.31.68',
    'localhost',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'sbhs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
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

ROOT_URLCONF = 'sbhs_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'sbhs_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

SLOT_DURATION = 55

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp-auth.iitb.ac.in'

EMAIL_PORT = 25

EMAIL_HOST_USER = credentials.EMAIL_HOST_USER

EMAIL_HOST_PASSWORD = credentials.EMAIL_HOST_PASSWORD

# Set EMAIL_BACKEND to 'django.core.mail.backends.smtp.EmailBackend'
# in production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SENDER_EMAIL, REPLY_EMAIL, PRODUCTION_URL, IS_DEVELOPMENT are used in email
# verification. Set the variables accordingly to avoid errors in production

# This email id will be used as <from address> for sending emails.
# For example no_reply@<your_organization>.in can be used.
SENDER_EMAIL = 'iakashchavan@gmail.com'

# Organisation/Indivudual Name.
SENDER_NAME = 'SBHS Team'

# This email id will be used by users to send their queries
# For example queries@<your_organization>.in can be used.
REPLY_EMAIL = 'mahesh_gudi@iitb.ac.in'

# This url will be used in email verification to create activation link.
# Add your hosted url to this variable.
# For example https://127.0.0.1:8000 or 127.0.0.1:8000
PRODUCTION_URL = '127.0.0.1:8000'


# Set this variable to <False> once the project is in production.
# If this variable is kept <True> in production, email will not be verified.
IS_DEVELOPMENT=False

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
