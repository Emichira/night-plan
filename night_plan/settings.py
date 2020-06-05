import os
import environ
import django_heroku

import re
from ctypes import CDLL, CFUNCTYPE, POINTER, Structure, c_char_p
from ctypes.util import find_library

from django.contrib.gis.geos.error import GEOSException
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import SimpleLazyObject

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nightplankenya.co.ke', 'www.nightplankenya.co.ke', 'localhost', 'nightplankenya.com', 'www.nightplankenya.com', '0.0.0.0', '127.0.0.1', 'https://nightplankenya.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'social_django',
    'crispy_forms',
    'whitenoise.runserver_nostatic',
    'storages',
    'django.contrib.sites',
    'django.contrib.humanize',
    'google_analytics',

    #My Apps
    'pages.apps.PagesConfig',
    'events.apps.EventsConfig',
    'categories.apps.CategoriesConfig',
    'event_types.apps.EventTypesConfig',
    'counties.apps.CountiesConfig',
    'contacts.apps.ContactsConfig',
    'clubs.apps.ClubsConfig',
    'genres.apps.GenresConfig',
    'alcohol.apps.AlcoholConfig',
    'blog_categories.apps.BlogCategoriesConfig',
    'blogs.apps.BlogsConfig',
    'cocktails.apps.CocktailsConfig',
    'drink_categories.apps.DrinkCategoriesConfig',
    'drink_glass_types.apps.DrinkGlassTypesConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.twitter',
]

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'night_plan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'night_plan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": 'django.contrib.gis.db.backends.postgis',
        'NAME': 'nightplan_db',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOST'),
        'PORT': os.environ.get('RDS_PORT'),
    }
}

import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
DATABASES['default'] = dj_database_url.config(default='postgis://postgres:M1ch$anuel!@localhost:5432/nightplan_db')
DATABASES['default'] = dj_database_url.parse('postgis://postgres:M1ch$anuel!@localhost:5432/nightplan_db', conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
## Settings specific for python-solical-auth
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
]

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Django-allauth configurations
LOGIN_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_BLACKLIST = ["nightplan", "admin", "god", "nightplankenya"]
ACCOUNT_USERNAME_MIN_LENGTH = 2
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GOOGLE_ANALYTICS = {
    'google_analytics_id': os.environ.get('GOOGLE_ANALYTICS_KEY'),
}

# #Change static storage to Amazon Web Services S3-static
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID_NIGHT')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY_NIGHT')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME_NIGHT')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
DEFAULT_FILE_STORAGE = 'night_plan.storage_backends.MediaStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
AWS_DEFAULT_ACL = None
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Old static storage settings
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
# STATIC_URL = '/static/'

#Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

#Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSW')
EMAIL_USE_TLS = True

#leaflet config
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-1.286389, 36.817223),
    'DEFAULT_ZOOM': 5,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'ATTRIBUTION_PREFIX': 'Night Plan Kenya',
    'SCALE': 'both',
    'RESET_VIEW': True,
    'boxZoom' : True,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

django_heroku.settings(locals())
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'