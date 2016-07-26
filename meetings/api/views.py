from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import viewsets
from api.serializers import AuthenticationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
import requests


class CheckLoggedInView(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated():
            return Response('true')
        else:
            return Response('false')


class CurrentUserView(APIView):
    base_url = '{}oauth2/{}'.format(OsfOauth2AdapterConfig.osf_accounts_url, '{}')
    access_token_url = base_url.format('token')
    authorize_url = base_url.format('authorize')
    profile_url = '{}v2/users/me/'.format(OsfOauth2AdapterConfig.osf_api_url)

    def get(self, request, **kwargs):
        if request.user.is_authenticated():
            curUser = request.user.username
            account = SocialAccount.objects.get(uid=curUser)
            token = SocialToken.objects.get(account=account)
            extra_data = requests.get(self.profile_url, headers={
                'Authorization': 'Bearer {}'.format(token)
            })
            return Response(extra_data.json())
        else:
            return Response('false')


class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDetail(APIView):
    resource_name = 'User'
    serializer_class = UserSerializer

    def get(self, request, user_id=None, format=None):
        user = User.objects.get(pk=user_id)
        user_serializer = UserSerializer(
            user,
            context={'request': request},
            many=False
        )
        return Response(user_serializer.data)


class AuthenticateUser(APIView):
    resource_name = 'User'
    serializer_class = AuthenticationSerializer

    def post(self, request, format=None):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # the authentication system was unable to verify the user
                return Response(
                    "The username and password were not found",
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                "Incorrect format for POST",
                status=status.HTTP_404_NOT_FOUND
            )
