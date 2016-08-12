import factory

from submissions.models import Submission
from approvals.models import Approval
from conferences.models import Conference
from django.contrib.auth.models import User
from requests.models import Response
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User


class ConferenceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Conference


class ApprovalFactory(factory.DjangoModelFactory):
    class Meta:
        model = Approval


class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Submission

    approval = factory.SubFactory(ApprovalFactory)


class SocialAccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = SocialAccount


class SocialTokenFactory(factory.DjangoModelFactory):
    class Meta:
        model = SocialToken


class SocialAppFactory(factory.DjangoModelFactory):
    class Meta:
        model = SocialApp


class ResponseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Response
