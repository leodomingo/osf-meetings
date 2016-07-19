from rest_framework_json_api import serializers
from rest_framework.reverse import reverse

from approvals.models import Approval
from django.contrib.auth.models import User

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
