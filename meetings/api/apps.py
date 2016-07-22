from __future__ import unicode_literals
from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    name = 'api'


class OsfOauth2AdapterConfig(AppConfig):
    name = 'osf_oauth2_adapter'
    # staging by default so people don't have to run OSF to use this.

    osf_api_url = settings.OSF_API_URL
    osf_accounts_url = settings.OSF_ACCOUNTS_URL
    default_scopes = settings.DEFAULT_SCOPES
    humans_group_name = settings.HUMANS_GROUP_NAME
