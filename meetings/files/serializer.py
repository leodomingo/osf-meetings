from rest_framework_json_api import serializers as ser

from files.models import File


class FileSerializer(ser.ModelSerializer):
    temp_file = ser.FileField()

    class Meta:
        model = File
