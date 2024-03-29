import os
import sys
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


# Add the local vendor libs path
sys.path.append(BASE_DIR + "/vendorlibs")


# DEFINE THE ENVIRONMENT TYPE
PRODUCTION = STAGE = DEMO = LOCAL = False
dt_key = os.environ.get('DEPLOYMENT_TYPE', 'LOCAL')
if dt_key == 'PRODUCTION':
    PRODUCTION = True
elif dt_key == 'DEMO':
    DEMO = True
elif dt_key == 'STAGE':
    STAGE = True
elif dt_key == 'LOCAL':
    LOCAL = True
else:
    raise Exception("Cannot find the DEPLOYMENT_TYPE environment variable. This is to be provided along with other vital env vars. If this instance is running locally, the '.env' file must be provided. If this instance is running on production, the environment variables have not been set up correctly. See the readme.md for more details.")


# Set up logger
if LOCAL:
    log_level = logging.DEBUG
elif PRODUCTION:
    log_level = logging.INFO
else:
    log_level = logging.DEBUG

logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

if LOCAL or STAGE:
    logging.getLogger('boto').setLevel(logging.INFO)
    logging.getLogger('pyqs').setLevel(logging.INFO)

logger.info("Deployment environment detected: {}".format(dt_key))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL or STAGE

AUTH_USER_MODEL = 'user.User'

WSGI_APPLICATION = 'settings.wsgi.application'

SITE_BASE_URL = os.environ.get('SITE_BASE_URL')

ALLOWED_HOSTS = [
    'itt-trade-stage.herokuapp.com',
    'itt-trade-production.herokuapp.com',
    'localhost',
]

# APPLICATION DEFINITION
INSTALLED_APPS = [
    # MAIN APPS
    'apps.common',
    'apps.user',
    'apps.signal',
    'apps.portfolio',

    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # PLUGINS

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

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(SITE_ROOT, 'templates'), ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.template.context_processors.media',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}, ]

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
    ('user', os.path.join(SITE_ROOT, 'apps/user/static')),
)

### START DJANGO ALLAUTH SETTINGS ###
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_ADAPTER = 'apps.user.my_adapter.MyAccountAdapter'

### END DJANGO ALLAUTH SETTINGS ###


# General apps settings

if PRODUCTION or STAGE:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

logger.info("Importing vendor_services_settings")
try:
    from settings.vendor_services_settings import *
except Exception as e:
    logger.warning("Failed to import vendor_services_settings.")
    logger.warning(str(e))


if LOCAL:
    logger.info("LOCAL environment detected. Importing local_settings.py")
    try:
        from settings.local_settings import *
    except:
        logger.error("Could not successfully import local_settings.py. This is necessary if you are running locally. This file should be in version control.")
        raise
