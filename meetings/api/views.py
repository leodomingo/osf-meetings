from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from meetings.utils import OsfOauth2AdapterConfig
from rest_framework import status
import requests
import json


class CheckLoggedInView(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated():
            return Response('true')
        else:
            return Response('false')


class CurrentUserView(APIView):
    base_url = '{}oauth2/{}'.format(
        OsfOauth2AdapterConfig.osf_accounts_url, '{}')
    access_token_url = base_url.format('token')
    authorize_url = base_url.format('authorize')
    profile_url = '{}v2/users/me/'.format(OsfOauth2AdapterConfig.osf_api_url)

    #  we need to save the user's info in a the user model instead of
    #  retrieving it all the time from osf

    def get(self, request, **kwargs):
        if request.user.is_authenticated():
            curUser = request.user.username
            account = SocialAccount.objects.get(uid=curUser)
            token = SocialToken.objects.get(account=account)

            extra_data = requests.get(self.profile_url, headers={
                'Authorization': 'Bearer {}'.format(token)
            })

            data = json.loads(extra_data._content)['data']
            data['id'] = request.user.id
            data['osf-id'] = curUser
            data['attributes']['token'] = str(token)

            return Response(data)
        else:
            return Response(
                'User is not logged in',
                status=status.HTTP_401_UNAUTHORIZED
            )
