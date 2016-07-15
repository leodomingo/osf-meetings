from __future__ import unicode_literals

from django.apps import AppConfig
import os

class OsfOauth2AdapterConfig(AppConfig):
    name = 'osf_oauth2_adapter'
    # staging by default so people don't have to run OSF to use this.
    osf_api_url = os.environ.get('OSF_API_URL', 'https://staging-api.osf.io').rstrip('/') + '/'
    osf_accounts_url = os.environ.get('OSF_ACCOUNTS_URL', 'https://staging-accounts.osf.io').rstrip('/') + '/'
    default_scopes = ['osf.full_write',]
    osf_users_group = 'OSF_USERS'