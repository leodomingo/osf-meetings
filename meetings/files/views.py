import ipdb
import json

from django.shortcuts import render
from conferences.models import Conference
from submissions.models import Submission
from rest_framework.viewsets import ModelViewSet
from files.serializer import FileSerializer
from files.models import File

from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount

import requests
from api.apps import OsfOauth2AdapterConfig

# Create your views here.

class FileViewSet(ModelViewSet):
    resource_name = 'files'

    queryset = File.objects.all()
    serializer_class = FileSerializer

    base_url = '{}oauth2/{}'.format(OsfOauth2AdapterConfig.osf_accounts_url, '{}')
    access_token_url = base_url.format('token')
    profile_url = '{}v2/users/me/'.format(OsfOauth2AdapterConfig.osf_api_url)
    waterbutler_url = '{}v1/resources/'.format(OsfOauth2AdapterConfig.osf_files_url)
    staging_url = '{}project/'.format(OsfOauth2AdapterConfig.osf_staging_url)

    def create(self, request):
        current_user = request.user.username
        account = SocialAccount.objects.get(uid=current_user)
        osf_token = SocialToken.objects.get(account=account)

        submission_obj = Submission.objects.get(id=request.data['submission_id'])

        file_url = '{}{}/providers/osfstorage'.format(self.waterbutler_url,
            submission_obj.node_id)

        file_stream = request.FILES['temp_file']

        upload_url = '{}/?kind=file&name={}'.format(file_url, file_stream.name)

        response = requests.put(
            upload_url,
            data=file_stream,
            headers = {
                'Authorization' : 'Bearer {}' . format(osf_token)
                }
            )

        res_json = json.loads(response.content)

        #pull the submission related to an user
        #multiple submissions?
        pass


