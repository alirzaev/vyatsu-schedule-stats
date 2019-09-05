import django_heroku

from .defaults import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'y&j5lh%apt1^reat=1bt^!womav75@6m#lsj99nkhtui-)&%i&'

django_heroku.settings(locals())
