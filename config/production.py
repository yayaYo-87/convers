from config.settings import *
DEBUG = False
ALLOWED_HOSTS = ['144.76.163.52']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'convers',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'USER': 'postgres',
    }
}

ADMINS = [
    ('Blackout', 'zubkov@smoothie.digital')
]

SITE_HOST = '144.76.163.52'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend
