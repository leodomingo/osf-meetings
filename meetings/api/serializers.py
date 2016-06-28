from django.contrib.auth.models import User, Group
from api.models import Submission, Conference
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name')

class ConferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conference
		fields = ('created', 'modified', 'id', 'title', 'website', 'city', 
			'state', 'country', 'start_date', 'end_date', 'submission_date', 'close_date', 'logo_url', 'tags', 'sponsors', 'description')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
	conference = serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all())
	contributors = UserSerializer(many=True)
	node_id = serializers.CharField(read_only=True)

	def create(self, validated_data):
		# look up contributors by ID
		contributors = validated_data['contributors']
		title = validated_data['title']
		description = validated_data['description']
		conference = validated_data['conference']
		submission = Submission.objects.create(title=title, description=description, conference=conference, approved=False)
		for contributor in contributors:
			submission.contributors.add(contributor)
		return submission


	class Meta:
		model = Submission
		fields = ('id', 'node_id', 'title', 'description', 'conference', 'contributors')