import ipdb
import json

from submissions.models import Submission
from rest_framework.viewsets import ModelViewSet
from files.serializer import FileSerializer
from files.models import File

from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount

import requests
from utils import OsfFileStorageUrls


class FileViewSet(ModelViewSet):
    resource_name = 'files'

    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request):
        current_user = request.user.username
        account = SocialAccount.objects.get(uid=current_user)
        osf_token = SocialToken.objects.get(account=account)

        submission_obj = Submission.objects.get(
            id=request.data['submission_id'])
        file_url = '{}{}/providers/osfstorage'.format(
            OsfFileStorageUrls.WATERBUTLER_URL, submission_obj.node_id)

        file_stream = request.FILES['temp_file']

        upload_url = '{}/?kind=file&name={}'.format(file_url, file_stream.name)

        response = requests.put(
            upload_url,
            data=file_stream,
            headers={
                'Authorization': 'Bearer {}'.format(osf_token)
            }
        )

        # res_json = json.loads(response.content)
        json.loads(response.content)
        ipdb.set_trace()

        # pull the submission related to an user
        # multiple submissions?
        pass
