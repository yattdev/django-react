"""
Django settings for django_react project.

Generated by 'django-admin startproject' using Django 2.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, environ
env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path helper
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', x)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p7z%t_$r2#s78z^s8xe9g8*ul13l_js@f$3)=x9$$r#_0gv&na'

# SECURITY WARNING: don't run with debug turned on in production!

if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = env.bool('DEBUG', default=False)
else:
    DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
#  ALLOWED_HOSTS = env.list('ALLOWED_HOSTS',
#  default=['alassane.herokuapp.com',
#  'www.alassane.herokuapp.com',
#  'localhost'])

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'weblog',
    'debug_toolbar',
    'bootstrap4',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_react.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'django_react.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jady_db',
        'USER': 'alassane',
        'PASSWORD': '7678_gone',
        'HOST': '',
        'PORT': 5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = location('staticfiles')

STATICFILES_DIRS = [
    location("static/"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# for debug_toolbar
INTERNAL_IPS = ['127.0.0.1']

if os.environ.get('ENV') == 'PRODUCTION':
    """ Sometimes Django apps are deployed at a particular prefix
    (or “subdirectory”) on a domain e.g. http://example.com/my-app/ rather than
    just http://example.com. In this case you would normally use Django’s
    FORCE_SCRIPT_NAME setting to tell the application where it is located
    """
    # FORCE_SCRIPT_NAME = '/blog'
    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    STATIC_ROOT = location('staticfiles')

    STATICFILES_DIRS = (location('static'), )

    # """ DROPBOX CONFIGURATION """
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

    # DROPBOX_OAUTH2_TOKEN = "QH8Mis-t1EAAAAAAAAAAEFd2xvWbp5-DkSc-7W5xzz-V9Me_EnzRMUXALHxeq-Oc"
    DROPBOX_OAUTH2_TOKEN = "QH8Mis-t1EAAAAAAAAAADfVvZ6NFX_7vNRJP2OX3HNmM1YlrRqXS9dbf_yyJiD-p"

    DROPBOX_ROOT_PATH = '/blog/'

    DROPBOX_OAUTH2_KEY = "uh51yq1xd4bj34t"

    DROPBOX_OAUTH2_SECRET = "d8qqrd3j3eypd5a"

    # DROPBOX_OAUTH2_KEY = "x6wtdz1yz5xe05j"

    # DROPBOX_OAUTH2_SECRET = "9nczp780kbzbgah"

    MEDIA_URL = '/blog/media/'
    MEDIA_ROOT = 'blog/media/'

    ADMIN_MEDIA_PREFIX = 'blog/media/'
    # "************ END DROPBOX CONFIGURATION ************"

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
    # whitenoise.storage.CompressedManifestStaticFilesStorage
    import dj_database_url

    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)