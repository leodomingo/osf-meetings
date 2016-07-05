from django.contrib.auth.models import User, Group
from api.models import Submission
from rest_framework import serializers as ser

from conferences.models import Conference

class UserSerializer(ser.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')

class GroupSerializer(ser.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class AuthenticationSerializer(ser.Serializer):
    username = ser.CharField(required=True)
    password = ser.CharField(required=True)

    def validate(self, data):
        return data


class SubmissionSerializer(ser.HyperlinkedModelSerializer):
    conference = ser.PrimaryKeyRelatedField(queryset=Conference.objects.all())
    contributors = UserSerializer(many=True)
    node_id = ser.CharField(read_only=True)

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
