from django.contrib.auth.models import User, Group
from rest_framework import generics
from api.serializers import UserSerializer, GroupSerializer
from api.models import Node, SubmissionEval, Meeting
from api.serializers import NodeSerializer, SubmissionEvalSerializer, MeetingSerializer
from rest_framework import generics
import requests
from requests_oauth2 import OAuth2
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse



USER_STORAGE = {}

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get(self, pk, request, format=None):
    	meeting = Meeting.objects.get(id=pk)
    	return Response(meeting)

class OsfAuthorizationUrl(APIView):
	def get(self, request, format=None):
		client_id  = 'd5c46638ed1d42b9977264d084875c5a'
		client_secret = 'Pxsc1AeBDHBNK5dNCrqjvYkonBKMXXSvNSoDyK84'
		oauth2_handler = OAuth2(client_id, client_secret, "https://staging-accounts.osf.io/", "http://localhost:8000/login", authorization_url='oauth2/authorize')
		authorization_url = oauth2_handler.authorize_url('osf.full_read osf.full_write', response_type='code')
		return Response(authorization_url)


class OsfAuthorizationCode(APIView):
	def get(self, request, format=None):
		client_id  = 'd5c46638ed1d42b9977264d084875c5a'
		client_secret = 'Pxsc1AeBDHBNK5dNCrqjvYkonBKMXXSvNSoDyK84'
		code = request.GET.get('code')
		USER_STORAGE[request.user] = code
		return Response(str(USER_STORAGE))

class NodeList(APIView):
	def get(self, request, format=None):
		user = request.user
		CLIENT_ID  = 'd5c46638ed1d42b9977264d084875c5a'
		CLIENT_SECRET = 'Pxsc1AeBDHBNK5dNCrqjvYkonBKMXXSvNSoDyK84'
		client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
		REDIRECT_URI = "http://localhost:8000/login"
		post_data = { "grant_type": "authorization_code", "code": USER_STORAGE[user], "redirect_uri": REDIRECT_URI }
		headers = {"Authorization" : "Bearer " + USER_STORAGE[user]}
		response = requests.get("https://staging-accounts.osf.io/oauth2/authorize", auth=client_auth, headers=headers)
		return Response(response)


class NodeDetail(APIView):
	def get(self, request, format=None):
		pass



