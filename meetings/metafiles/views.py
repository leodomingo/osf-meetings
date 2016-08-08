from rest_framework.response import Response

from submissions.models import Submission
from rest_framework.viewsets import ModelViewSet
from metafiles.serializers import MetafileSerializer
from metafiles.models import Metafile


class MetafileViewSet(ModelViewSet):
    resource_name = 'metafiles'

    queryset = Metafile.objects.all()
    serializer_class = MetafileSerializer

    def create(self, request, *args, **kwargs):
        metafileSer = MetafileSerializer(
            data=request.data,
            context={'request': request}
        )

        if metafileSer.is_valid():
            metafileSer.save(
                owner=request.user,
                submission=Submission.objects.get(
                    contributor=request.user.id
                )
            )
            return Response(metafileSer.data)
        return Response(metafileSer.errors)
