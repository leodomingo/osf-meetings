from django.test import TestCase, RequestFactory
from unittest import skip
import factory
from conferences.models import Conference
from approvals import models as approvalModels
from submissions import models as submissionModels
from django.contrib.auth.models import User
from permissions import ConferencePermissions
from serializers import ConferenceSerializer
from views import ConferenceViewSet
from django.utils.functional import SimpleLazyObject

class UserFactory(factory.DjangoModelFactory):
    class Meta: 
        model = User

class ConferenceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Conference


class ApprovalFactory(factory.DjangoModelFactory):
    class Meta:
        model = approvalModels.Approval


class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = submissionModels.Submission

    #filling out NON NULL field
    approval = factory.SubFactory(ApprovalFactory)
# TODO: Ask Jesse how permissions work
# class TestPermissions(TestCase):
#     def setUp(self):
#         self.user1 = UserFactory(id='userONE')
#         self.user2 = UserFactory(id='userTWO')
#         self.conference = ConferenceFactory(
#             admin = self.user1
#         )
#         self.request1 = RequestFactory().get('./fake_path')
#         self.request2 = RequestFactory().get('./fake_path')


#     def test_conference_creator(self):
#         self.view = ConferenceViewSet()
#         self.request1.user = self.user1
#         self.request2.user = self.user2
#         self.confPermissions = ConferencePermissions()
#         self.permissions1 = self.confPermissions.has_permission(self.request1, self.view)
#         self.permissiosn2 = self.confPermissions.has_permission(self.request2, self.view)
#         print(self.permissions1.get_object())

class TestSerializers(TestCase):
    def setUp(self):
        self.user1 = UserFactory(
            username = 'Leo',
            id = '99'
            )
        self.user2 = UserFactory(
            username = 'LeoLeo'
            )
        self.conference = ConferenceFactory(
            admin = self.user1
        )
        self.submission1 = SubmissionFactory(
            conference = self.conference,
            contributor = factory.SubFactory(UserFactory, username='Tom')
            )
        self.submission2 = SubmissionFactory(
            conference = self.conference,
            contributor = factory.SubFactory(UserFactory, username='User2')
            )
        # self.request1 = RequestFactory().post('./fake_path')
        # self.request1.user = SimpleLazyObject(self.user1)
        # self.request1.query_params = {}
        # self.request2 = RequestFactory().post('./fake_path')
        # self.request2.user = SimpleLazyObject(self.user2)
        # self.request2.query_params = {}


    @skip('Test links are formed correctly')
    def test_get_links(self):
        pass

    def test_get_submission_count(self):
        self.serializer = ConferenceSerializer()
        self.assertEqual(self.serializer.get_submission_count(self.conference), 2)
        self.assertFalse(self.serializer.get_submission_count(self.conference) == 5)

    # The problem here is that the get_can_edit function calls User.objects and our factory_boy objects
    # aren't showing up in the User.objects 
    # def test_get_can_edit(self):
    #     self.serializer1 = ConferenceSerializer(context={'request': self.request1})
    #     self.serializer2 = ConferenceSerializer(context={'request': self.request2})
    #     self.canEdit1 = self.serializer1.get_can_edit(self.conference)
    #     self.canEdit2 = self.serializer2.get_can_edit(self.conference)
    #     self.assertTrue(self.canEdit1)
    #     self.assertTrue(self.canEdit2)


class TestSignals(TestCase):
    @skip('Test that permissions are added correctly')
    def test_add_permissions(self):
        pass


class TestViews(TestCase):
    @skip('Test create')
    def test_create(self):
        pass

    @skip('Test perform_create')
    def test_perform_create(self):
        pass
