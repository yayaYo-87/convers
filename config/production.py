from config.settings import *
DEBUG = False
ALLOWED_HOSTS = ['classicalbooks.ru', 'www.classicalbooks.ru', 'classical-books.ru', 'классическиекниги.рф', 
'классические-книги.рф',
'classicalConversationsbooks.com','www.classical-books.ru', 'www.классическиекниги.рф', 'www.классические-книги.рф',
'www.classicalconversationsbooks.com']

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

SITE_HOST = 'classicalbooks.ru'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SERVER_EMAIL = EMAIL_HOST_USER
TINKOFF_PASSWORD=os.environ.get('TINKOFF_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
