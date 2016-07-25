from rest_framework import viewsets
from rest_framework import filters
from conferences.models import Conference
from conferences.serializers import ConferenceSerializer
from conferences.permissions import ConferencePermissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
