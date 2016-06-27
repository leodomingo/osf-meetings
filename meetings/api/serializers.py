from django.contrib.auth.models import User, Group
from api.models import Submission, Conference, Tag
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name')

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'lower',)

class ConferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conference
		fields = ('created', 'modified', 'id', 'title', 'website', 'city', 
			'state', 'country', 'start_date', 'end_date', 'submission_date', 'close_date', 'logo_url', 'tags', 'sponsors', 'description')

class SubmissionSerializer(serializers.ModelSerializer):
	conference = ConferenceSerializer()
	tags = TagSerializer(many=True)
	contributors = GroupSerializer()
	node_id = serializers.CharField(read_only=True)
	class Meta:
		model = Submission
		fields = ('id', 'node_id', 'title', 'description', 'conference', 'tags', 'contributors')