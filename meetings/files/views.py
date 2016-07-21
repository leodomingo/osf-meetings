import ipdb

from django.shortcuts import render
from conferences.models import Conference
from rest_framework.viewsets import ModelViewSet
from files.serializer import FileSerializer
from files.models import File

# Create your views here.

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, request, serializer):
        ipdb.set_trace()
        pass


