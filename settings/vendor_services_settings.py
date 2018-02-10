import os

import dj_database_url

from settings import LOCAL, PRODUCTION, STAGE

if not LOCAL:

    DATABASES = {'default': dj_database_url.config()}

    # AWS
    BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_OPTIONS = {
        'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
        'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
        'AWS_STORAGE_BUCKET_NAME': BUCKET_NAME,
        'AWS_SNS_TOPIC': os.environ.get('AWS_SNS_TOPIC'),
    }

    HOST_URL = 'http://' + BUCKET_NAME + '.s3.amazonaws.com'
    MEDIA_URL = 'http://' + BUCKET_NAME + '.s3.amazonaws.com/'
    AWS_STATIC_URL = 'http://' + BUCKET_NAME + '.s3.amazonaws.com/'
    STATIC_ROOT = STATIC_URL = AWS_STATIC_URL
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
