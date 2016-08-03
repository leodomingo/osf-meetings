from rest_framework.response import Response

from submissions.models import Submission
from rest_framework.viewsets import ModelViewSet
from files.serializer import FileSerializer
from files.models import File


class FileViewSet(ModelViewSet):
    resource_name = 'files'

    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):

        fileSer = FileSerializer(
            data=request.data,
            context={'request': request}
        )

        if fileSer.is_valid():
            fileSer.save(
                owner=request.user,
                submission=Submission.objects.get(
                    contributor=request.user.id
                )
            )
            return Response(fileSer.data)
        return Response(fileSer.errors)
