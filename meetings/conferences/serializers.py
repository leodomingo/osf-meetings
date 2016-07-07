from rest_framework_json_api import serializers

from conferences.models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
