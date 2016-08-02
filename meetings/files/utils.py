from __future__ import unicode_literals
from django.apps import AppConfig
from meetings.utils import OsfOauth2AdapterConfig


class OsfFileStorageUrls(AppConfig):
    BASE_URL = '{}oauth2/{}'.format(OsfOauth2AdapterConfig.osf_accounts_url, '{}')
    ACCESS_TOKEN_URL = BASE_URL.format('token')
    PROFILE_URL = '{}v2/users/me/'.format(OsfOauth2AdapterConfig.osf_api_url)
    WATERBUTLER_URL = '{}v1/resources/'.format(OsfOauth2AdapterConfig.osf_files_url)
    PROJECTS_URL = '{}project/'.format(OsfOauth2AdapterConfig.osf_staging_url)
