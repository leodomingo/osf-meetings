from django.contrib.auth.models import User, Group
from rest_framework import generics
from api.serializers import UserSerializer, GroupSerializer
from api.models import Node, SubmissionEval, Meeting
from api.serializers import NodeSerializer, SubmissionEvalSerializer, MeetingSerializer
from rest_framework import generics
import requests
from requests_oauth2 import OAuth2

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

def NodeList(self):
	client_id  = '8bce2d2ed769427dbfbf3d3ca29f78b6'
	client_secret = '2ZKQkpjcR23k3ECZME83jfxZ5wnoO3vo3uqQjRA3'

	oauth2_handler = OAuth2(client_id, client_secret, "https://staging.osf.io", "localhost:4200/login")

	authorization_url = oauth2_handler.authorize_url('osf.full_read, osf.full_write')

	response = oauth2_handler.get_token(authorization_url)

	print(response)

	# oauth2_client = requests.session(params={'access_token': response['access_token']})
	# osf_response = oauth2_client.get('https://staging-api.osf.io/v2/nodes')
	return osf_response


def NodeDetail(self):
	client_key  = ''
	client_secret = ''
	resource_owner_key = ''
	resource_owner_secret = ''
	url = 'http://?'
