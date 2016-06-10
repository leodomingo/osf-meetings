from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Node, SubmissionEval, Meeting
from api.serializers import NodeSerializer, SubmissionEvalSerializer, MeetingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nodes to be viewed or edited.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

@api_view(['GET', 'POST'])
def node_list(request):
    if request.method == 'GET':
        nodes = Node.objects.all()
        serializers = NodeSerializer(nodes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubmissionEvalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows submission-evals to be viewed or edited.
    """
    queryset = SubmissionEval.objects.all()
    serializer_class = SubmissionEvalSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows submission-evals to be viewed or edited.
    """
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer