from django.contrib.auth.models import User, Group
from api.models import Node, SubmissionEval, Conference
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class NodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Node
		fields = ('id', 'title', 'contributors', 'description','keywords')


class SubmissionEvalSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubmissionEval
		fields = ('id', 'created', 'premise', 'research','style', 'comment', 'total')

class ConferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conference
		fields = ('created', 'modified', 'id', 'title', 'website', 'city', 
			'state', 'country', 'start_date', 'end_date', 'submission_date', 'close_date', 'logo_url', 'tags', 'sponsors', 'description')
