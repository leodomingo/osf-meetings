from django.http import Http404
from rest_framework_json_api.views import RelationshipView
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters 
from conferences.models import Conference
from conferences.serializers import ConferenceSerializer
from conferences.permissions import ConferencePermissions

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
from rest_framework.permissions import IsAuthenticatedOrReadOnly 

# List of conferences
class ConferenceViewSet(viewsets.ModelViewSet):
    resource_name = 'conferences'
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoObjectPermissionsFilter,)
    permission_classes = (ConferencePermissions, )
    search_fields = ('title', 'description')

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        return super(ConferenceViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        serializer.save(admin=serializer.context['request'].user)


## Detail of a conference
#class ConferenceDetail(APIView):
#    resource_name = 'conference'
#
#    def get_object(self, pk):
#        try:
#            return Conference.objects.get(pk=pk)
#        except Conference.DoesNotExist:
#            raise Http404
#
#    def get(self, request, pk, format=None):
#        conference = self.get_object(pk)
#        serializer = ConferenceSerializer(conference, context={'request': request})
#        return Response(serializer.data)
#
#class ConferenceRelationshipView(RelationshipView):
#    queryset = Conference.objects
