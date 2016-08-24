import requests
from django.conf import settings

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2LoginView,
    OAuth2CallbackView,
)

from osf_oauth2_adapter.provider import OSFProvider


class OSFOAuth2Adapter(OAuth2Adapter):
    #  Used for Django All OAuth
    provider_id = OSFProvider.id
    base_url = '{}oauth2/{}'.format(settings.OSF_ACCOUNTS_URL, '{}')
    access_token_url = base_url.format('token')
    authorize_url = base_url.format('authorize')

    def complete_login(self, request, app, access_token, **kwargs):
        extra_data = requests.get(settings.PROFILE_URL, headers={
            'Authorization': 'Bearer {}'.format(access_token.token)
        })

        jsonData = extra_data.json()
        response = self.get_provider().sociallogin_from_response(
            request,
            jsonData
        )
        return response

oauth2_login = OAuth2LoginView.adapter_view(OSFOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(OSFOAuth2Adapter)
