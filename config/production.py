from config.settings import *
DEBUG = False
ALLOWED_HOSTS = ['classicalbooks.ru', 'www.classicalbooks.ru', 'classical-books.ru', 'классическиекниги.рф', 
'классические-книги.рф',
'classicalConversationsbooks.com','www.classical-books.ru', 'www.классическиекниги.рф', 'www.классические-книги.рф',
'www.classicalconversationsbooks.com', '144.76.163.52']

DATABASE_PASSWORD=os.environ.get('DATABASE_PASSWORD')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'convers',
        'PASSWORD': 1111,
        'HOST': 'localhost',
        'USER': 'postgres',
    }
}

ADMINS = [
    ('Blackout', 'zubkov@smoothie.digital')
]

SITE_HOST = 'classicalbooks.ru'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@classicalbooks.ru'
EMAIL_HOST_PASSWORD = HOST_PASSWORD

SERVER_EMAIL = EMAIL_HOST_USER
TINKOFF_PASSWORD=os.environ.get('TINKOFF_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}
