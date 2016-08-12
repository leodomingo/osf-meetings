import json

from rest_framework.response import Response
from rest_framework import viewsets, filters

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from submissions.permissions import SubmissionPermissions

from submissions.serializers import SubmissionSerializer

from submissions.models import Submission
from approvals.models import Approval
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount

import requests
from django.conf import settings

# from django.http import HttpResponse


class SubmissionViewSet(viewsets.ModelViewSet):
    resource_name = 'submissions'
    serializer_class = SubmissionSerializer
    lookup_url_kwarg = 'submission_id'
    lookup_field = 'pk'
    permission_classes = (SubmissionPermissions,)

    filter_backends = (
        filters.DjangoFilterBackend, filters.DjangoObjectPermissionsFilter)

    filter_fields = ('conference', 'contributor')
    queryset = Submission.objects.all()

    #  OSF's node url
    node_url = '{}v2/nodes/'.format(settings.OSF_API_URL)

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = SubmissionSerializer(
                data=request.data,
                context={'request': request}
            )
            new_approval = Approval.objects.create()
            contributor = request.user

            account = SocialAccount.objects.get(uid=request.user.username)
            osf_token = SocialToken.objects.get(account=account)

        if serializer.is_valid():
            # Creates a OSF's node
            node = {
                'data': {
                    'attributes': {
                        'category': 'project',
                        'description': request.data['description'],
                        'title': request.data['title']
                    },
                    'type': 'nodes'
                }
            }

            response = requests.post(
                self.node_url,
                data=json.dumps(node),
                headers={
                    'Authorization': 'Bearer {}'.format(osf_token),
                    'Content-Type': 'application/json; charset=UTF-8'
                }
            )

            response_osf = response.json()
            serializer.save(
                contributor=contributor,
                approval=new_approval,
                node_id=response_osf['data']['id']
            )
            return Response(serializer.data)
        return Response(serializer.errors)

    @method_decorator(login_required)
    def update(self, request, *args, **kwargs):
        current_user = request.user.username
        account = SocialAccount.objects.get(uid=current_user)
        osf_token = SocialToken.objects.get(account=account)

        update_node = {
            'data': {
                'attributes': {
                    'category': 'project',
                    'title': request.data['title']
                },
                'type': 'nodes',
                'id': request.data['node_id']
            }
        }

        # Update OSF's node
        response = requests.put(
            '{}{}/'.format(self.node_url, request.data['node_id']),
            data=json.dumps(update_node),
            headers={
                'Authorization': 'Bearer {}'.format(osf_token),
                'Content-Type': 'application/json; charset=UTF-8'
            }
        )

        if (response.status_code == 200):
            return super(SubmissionViewSet, self).update(request, args, kwargs)
        return Response(response.text, status=response.status_code)
