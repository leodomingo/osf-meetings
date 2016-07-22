from rest_framework.response import Response
from rest_framework import viewsets

from submissions.serializers import SubmissionSerializer
from submissions.models import Submission
from approvals.models import Approval
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    encoding = 'utf-8'
    lookup_url_kwarg = 'submission_id'
    lookup_field = 'pk'

    def get_queryset(self):
        conference_id = self.kwargs.get('conference_id')
        return Submission.objects.filter(conference_id=conference_id)

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        serializer = SubmissionSerializer(data=request.data,
                                          context={'request': request})
        new_approval = Approval.objects.create()
        contributor = request.user
        if not request.user.has_perm('submissions.can_set_contributor'):
            if serializer.is_valid():
                serializer.save(contributor=contributor, approval=new_approval)
                return Response(serializer.data)
        else:
            # email submissions can set contributor
            if serializer.is_valid():
                serializer.save(approval=new_approval)
                return Response(serializer.data)

        return Response(serializer.errors)
