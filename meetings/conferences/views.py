from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters 
from conferences.models import Conference
from conferences.serializers import ConferenceSerializer
from conferences.permissions import CustomObjectPermissions

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoObjectPermissions

# List of conferences
class ConferenceViewSet(viewsets.ModelViewSet):
    resource_name = 'conferences'
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('title', 'description')

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        return super(ConferenceViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        serializer.save(admin=serializer.context['request'].user)