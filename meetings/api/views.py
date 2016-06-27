from django.contrib.auth.models import User, Group
from rest_framework import generics
from api.serializers import UserSerializer, GroupSerializer
from api.models import Node, SubmissionEval, Conference
from api.serializers import NodeSerializer, SubmissionEvalSerializer, ConferenceSerializer
from rest_framework import generics
import requests
from requests_oauth2 import OAuth2
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse



USER_STORAGE = {}

class ConferenceList(generics.ListCreateAPIView):
    view_category = 'conference'
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

    def get(self, pk, request, format=None):
    	conference = Conference.objects.get(id=pk)
    	return Response(conference)

class OsfAuthorizationUrl(APIView):
	def get(self, request, format=None):
		client_id  = 'd5c46638ed1d42b9977264d084875c5a'
		client_secret = 'Pxsc1AeBDHBNK5dNCrqjvYkonBKMXXSvNSoDyK84'
		oauth2_handler = OAuth2(client_id, client_secret, "https://staging-accounts.osf.io/", "http://localhost:8000/login", authorization_url='oauth2/authorize')
		authorization_url = oauth2_handler.authorize_url('osf.full_read osf.full_write', response_type='code')
		return Response(authorization_url)


class OsfAuthorizationCode(APIView):
	def get(self, request, format=None):
		uid = request.user.id
		CLIENT_ID  = 'd5c46638ed1d42b9977264d084875c5a'
		CLIENT_SECRET = 'Pxsc1AeBDHBNK5dNCrqjvYkonBKMXXSvNSoDyK84'
		REDIRECT_URI = "http://localhost:8000/login"
		code = request.GET.get('code')
		post_data = { "grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
		headers = {"Authorization" : "Bearer " + code}
		response = requests.post("https://staging-accounts.osf.io/oauth2/token", data=post_data)
		USER_STORAGE[uid] = response
		return Response(USER_STORAGE[uid])

class NodeList(APIView):
	def get(self, request, format=None):
		
		
		return Response(response)


class NodeDetail(APIView):
	def get(self, request, format=None):
		pass



