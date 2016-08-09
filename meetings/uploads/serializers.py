from rest_framework_json_api import serializers as ser

from .models import Upload


class UploadSerializer(ser.ModelSerializer):
    owner = ser.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Upload
