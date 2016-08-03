from rest_framework_json_api import serializers as ser
from rest_framework_json_api.relations import ResourceRelatedField

from files.models import File
from django.contrib.auth.models import User
from submissions.models import Submission


class FileSerializer(ser.ModelSerializer):
    #  temp_file = ser.FileField(required=False)

    owner = ResourceRelatedField(
                queryset=User.objects.all(),
                required=False,
                allow_null=True)
    submission = ResourceRelatedField(
                    queryset=Submission.objects.all(),
                    required=False,
                    allow_null=True)

    class Meta:
        model = File
