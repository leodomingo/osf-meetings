from rest_framework_json_api import serializers as ser
from rest_framework.reverse import reverse
from rest_framework_json_api.relations import ResourceRelatedField

from submissions.models import Submission
from conferences.models import Conference
from approvals.models import Approval
from django.contrib.auth.models import User
from api.serializers import UserSerializer


class SubmissionSerializer(ser.ModelSerializer):
    #    include_serializers = {
    #        'conference' : 'conferences.serializers.ConferenceSerializer'
    #    }

    links = ser.SerializerMethodField()
    can_edit = ser.SerializerMethodField()
    node_id = ser.CharField(read_only=True)
    contributor = ResourceRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True)
    approval = ResourceRelatedField(
        queryset=Approval.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Submission

#    conference = ResourceRelatedField(
#        queryset=Conference.objects,
#        related_link_view_name='conference:submission:list',
#        related_link_url_kwarg='submission_id',
#        self_link_view_name='submission-relationships'
#    )

#    def create(self, validated_data):
#        # look up contributors by ID
#        submission = Submission.objects.create(title=title, description=description, conference=conference, approved=False)
#        for contributor in contributors:
#                submission.contributors.add(contributor)
#        return submission

    def get_links(self, obj):
        request = self.context.get('request')
        return {
            'self': reverse(
                'conferences:submissions:detail',
                kwargs={
                    'conference_id': obj.conference.id,
                    'submission_id': obj.pk
                },
                request=request
            ),
            'conference': reverse(
                'conferences:detail',
                kwargs={'pk': obj.conference.id},
                request=request
            ),
        }

    def get_can_edit(self, obj):
        request = self.context.get('request')
        user = request.user
        return (user == obj.contributor or user == obj.conference.admin)
