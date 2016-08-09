from rest_framework_json_api import serializers as ser
from rest_framework.reverse import reverse
from rest_framework_json_api.relations import ResourceRelatedField

from django.contrib.auth.models import User
from .models import Upload


class UploadSerializer(ser.ModelSerializer):
    owner = ser.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Upload
