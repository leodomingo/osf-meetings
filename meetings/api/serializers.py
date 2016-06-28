from django.contrib.auth.models import User, Group
from api.models import Submission, Conference
from rest_framework import serializers as ser
from django_countries.fields import CountryField


class UserSerializer(ser.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(ser.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class SubmissionSerializer(ser.ModelSerializer):
	class Meta:
		model = Submission
		fields = ('id', 'osf_id', 'title', 'contributors', 'description','tags', 'meeting')

class ConferenceSerializer(ser.ModelSerializer):
    title = ser.CharField(required=True)
    city = ser.CharField(required=True)
    state = ser.CharField(required=True)
    country = CountryField() #get country_dict working later
    event_start = ser.DateTimeField(required=True)
    event_end = ser.DateTimeField(required=True)
    submission_start = ser.DateTimeField(required=True)
    submission_end = ser.DateTimeField(required=True)
    logo_url = ser.URLField(required=True)
    description = ser.CharField(required=True)
    site_url = ser.URLField(required=False)

    class Meta:
        model = Conference
        fields = ('created', 'modified', 'id', 'title', 'site_url', 'city', 'state', 'country', 'event_start', 'event_end', 'submission_start', 'submission_end', 'logo_url', 'description')
