from rest_framework_json_api import serializers as ser
from rest_framework_json_api.relations import ResourceRelatedField

from metafiles.models import Metafile
from django.contrib.auth.models import User
from submissions.models import Submission


class MetafileSerializer(ser.ModelSerializer):
    owner = ResourceRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True
    )
    submission = ResourceRelatedField(
        queryset=Submission.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Metafile
