"""Copy this file into local.py for local development"""


SECRET_KEY = ''  # Set to large random value in your local.py
DEBUG = True
CLIENT_ID = ''
CLIENT_SECRET = ''

OSF_API_URL = ('https://staging-api.osf.io').rstrip('/') + '/'
OSF_ACCOUNTS_URL = ('https://staging-accounts.osf.io').rstrip('/') + '/'
DEFAULT_SCOPES = ['osf.full_write', ]
HUMANS_GROUP_NAME = 'OSF_USERS'

# Database
# POSTGRES_NAME = ''
# POSTGRES_USER = ''
# POSTGRES_PASSWORD = ''
# POSTGRES_HOST = ''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': POSTGRES_NAME,
#         'USER': POSTGRES_USER,
#         'PASSWORD': POSTGRES_PASSWORD,
#         'HOST': POSTGRES_HOST,
#         'PORT': '',
#     }
# }
