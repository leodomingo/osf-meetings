"""Copy this file into local.py for local development"""

from defaults import BASE_DIR
import os


SECRET_KEY = ''  # Set to large random value in your local.py
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}
