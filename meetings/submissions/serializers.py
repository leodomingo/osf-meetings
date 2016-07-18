from rest_framework_json_api import serializers as ser
from rest_framework.reverse import reverse

from submissions.models import Submission
from conferences.models import Conference
from django.contrib.auth.models import User
from api.serializers import UserSerializer


class SubmissionSerializer(ser.ModelSerializer):
    links = ser.SerializerMethodField()
    node_id = ser.CharField(read_only=True)
    contributor = ser.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    approved = ser.NullBooleanField(required=False)

    class Meta:
        model = Submission
        fields = ('id', 'node_id', 'title', 'description', 'conference',
                  'contributor', 'links', 'approved')

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
