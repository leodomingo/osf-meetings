from uploads.serializers import UploadSerializer
from uploads.models import Upload
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.


class UploadViewSet(viewsets.ModelViewSet):
    resource_name = 'uploads'
    serializer_class = UploadSerializer
    lookup_field = 'pk'
    filter_fields = ('owner',)
    queryset = Upload.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        return super(UploadViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=serializer.context['request'].user)
