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
        metafile_ser = MetafileSerializer(
            data=request.data,
            context={'request': request}
        )

        if metafile_ser.is_valid():
            submission_data = request.data['submission']
            submission_id = submission_data.items()[1][1]
            metafile_ser.save(
                owner=request.user,
                submission=Submission.objects.get(
                    id=submission_id
                )
            )
            return Response(metafile_ser.data)
        return Response(metafile_ser.errors)
