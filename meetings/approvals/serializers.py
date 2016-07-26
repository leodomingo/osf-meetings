from rest_framework_json_api import serializers

from approvals.models import Approval


class ApprovalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Approval
