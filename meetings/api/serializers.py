from django.contrib.auth.models import User, Group
from api.models import Submission, Meeting
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class SubmissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Submission
		fields = ('id', 'osf_id', 'title', 'contributors', 'description','tags', 'meeting')

class MeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting
		fields = ('id', 'title', 'website', 'city', 
			'state', 'country', 'start_date', 'end_date', 
			'submission_date', 'close_date', 'logo_url', 'tags', 'sponsors', 'description')