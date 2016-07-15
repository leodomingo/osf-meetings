from rest_framework_json_api import serializers
from rest_framework.reverse import reverse

from conferences.models import Conference
from django.contrib.auth.models import User

class ConferenceSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    admin = serializers.PrimaryKeyRelatedField(read_only=True)

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

    def get_can_edit(self, obj):
        request = self.context.get('request')
        user = User.objects.get(username=request.user)
        return user == obj.admin
