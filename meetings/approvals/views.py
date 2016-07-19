from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from approvals.models import Approval
from approvals.serializers import ApprovalSerializer

# Create your views here.

class ApprovalViewSet(viewsets.ModelViewSet):
    resource_name = 'approvals'
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    filter_backends = (filters.DjangoObjectPermissionsFilter,)
    permission_classes = (permissions.DjangoObjectPermissions,)
