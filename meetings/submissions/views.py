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
from rest_framework import status
from django.conf import settings


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
    node_url = settings.OSF_API_URL.format('v2/nodes/')

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

            if not request.user.has_perm('submissions.can_set_contributor'):
                if serializer.is_valid():
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
                                'Content-Type':
                                    'application/json; charset=UTF-8'
                            }
                    )

                    response_object = response.json()
                    serializer.save(
                        contributor=contributor,
                        approval=new_approval,
                        node_id=response_object['data']['id']
                    )
                    return Response(serializer.data)
            else:
                if serializer.is_valid():
                    serializer.save(approval=new_approval)
                    return Response(serializer.data)
            return Response(serializer.errors)
        return Response(
            {
                'error': 'Please login or signup',
                'status': 401
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
