from rest_framework import viewsets
from rest_framework import filters
from conferences.models import Conference
from conferences.serializers import ConferenceSerializer
from conferences.permissions import ConferencePermissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class ConferenceViewSet(viewsets.ModelViewSet):

    """ Conference Resource """

    resource_name = 'conferences'
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.DjangoObjectPermissionsFilter,)
    permission_classes = (ConferencePermissions, )
    search_fields = ('title', 'description')

    def retrieve(self, request, pk=None):
        """Returns a single Conference item"""
        return super(ConferenceViewSet, self).retrieve(request, pk)

    def update(self, request, *args, **kwargs):
        """Updates a single Conference item"""
        return super(ConferenceViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partial update a Conference """
        return super(ConferenceViewSet, self).partial_update(
            request, *args, **kwargs)

    def destroy(self, request, pk=None):
        """Delete a Conference"""
        return super(ConferenceViewSet, self).destroy(request, pk)

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        """
        Create a Conference
        """
        return super(ConferenceViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = User.objects.get(
                username=serializer.context['request'].user)
            serializer.save(admin=user)
