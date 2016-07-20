from rest_framework_json_api import serializers
from rest_framework.reverse import reverse

from conferences.models import Conference
from submissions.models import Submission



class ConferenceSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    submission_count = serializers.SerializerMethodField()

    class Meta:
        model = Conference

    def get_links(self, obj):
        request = self.context.get('request')
        return {
            'self': reverse(
                'conferences:detail',
                kwargs={'pk': obj.pk},
                request=request
            ),
            'submissions': reverse(
                'conferences:submissions:list',
                kwargs={'conference_id': obj.pk},
                request=request
            )
        }

    def get_submission_count(self, obj):
        return len(Submission.objects.filter(conference=obj))
