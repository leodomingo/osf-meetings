from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from rest_framework import status
import requests
import json
from django.conf import settings


class CurrentUserView(APIView):
    #  we need to save the user's info in a the user model instead of
    #  retrieving it all the time from osf
    def get(self, request, **kwargs):
        if request.user.is_authenticated():
            curUser = request.user.username
            account = SocialAccount.objects.get(uid=curUser)
            token = SocialToken.objects.get(account=account)

            # Gets the user's data
            extra_data = requests.get(
                settings.PROFILE_URL,
                headers={
                    'Authorization': 'Bearer {}'.format(token)
                }
            )

            data = json.loads(extra_data._content)['data']
            data['id'] = request.user.id
            data['osf-id'] = curUser
            data['attributes']['token'] = str(token)

            return Response(data)
        return Response(
            {
                'error': 'Please login or signup',
                'status': 401
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
