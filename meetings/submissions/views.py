import json

from rest_framework.response import Response
from rest_framework import viewsets, filters
# from rest_framework_json_api.views import RelationshipView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from submissions.permissions import SubmissionPermissions

from submissions.serializers import SubmissionSerializer

from submissions.models import Submission
from approvals.models import Approval
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount

import requests
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig

#
#   Basic ModelViewSet functions are expanded
#   so SwaggerUI can catch the description
#


class SubmissionViewSet(viewsets.ModelViewSet):

    """ Submission Resource """

    resource_name = 'submissions'
    serializer_class = SubmissionSerializer
    lookup_url_kwarg = 'submission_id'
    lookup_field = 'pk'
    permission_classes = (SubmissionPermissions,)
    filter_backends = (
        filters.DjangoFilterBackend, filters.DjangoObjectPermissionsFilter)
    filter_fields = ('conference', 'contributor')
    queryset = Submission.objects.all()

    base_url = '{}oauth2/{}'.format(
        OsfOauth2AdapterConfig.osf_accounts_url, '{}')
    access_token_url = base_url.format('token')
    profile_url = '{}v2/users/me/'.format(OsfOauth2AdapterConfig.osf_api_url)
    node_url = '{}v2/nodes/'.format(OsfOauth2AdapterConfig.osf_api_url)

    def list(self, request):
        return super(SubmissionViewSet, self).list(self, request)

    def retrieve(self, request, pk=None):
        """Returns a single Submission item"""
        return super(SubmissionViewSet, self).retrieve(request, pk)

    def update(self, request, *args, **kwargs):
        """Updates a single Submission item"""
        return super(SubmissionViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partial update a Submission """
        return super(SubmissionViewSet, self).partial_update(
            request, *args, **kwargs)

    def destroy(self, request, pk=None):
        """Delete a Submission"""
        return super(SubmissionViewSet, self).destroy(request, pk)

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        """ Create a Submission """
        serializer = SubmissionSerializer(
            data=request.data, context={'request': request})
        new_approval = Approval.objects.create()
        contributor = request.user

        current_user = request.user.username
        account = SocialAccount.objects.get(uid=current_user)
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
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Accept': 'application/json, text/*'
                    }
                )

                obj = response.json()
                serializer.save(
                    contributor=contributor,
                    approval=new_approval,
                    node_id=obj['data']['id']
                )

                return Response(serializer.data)
        else:
            if serializer.is_valid():
                serializer.save(approval=new_approval)
                return Response(serializer.data)
        return Response(serializer.errors)
