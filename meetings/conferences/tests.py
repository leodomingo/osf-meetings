from django.test import TestCase, RequestFactory
from unittest import skip
import factory
from . import models
from permissions import ConferencePermissions
from serializers import ConferenceSerializer
from views import ConferenceViewSet
from django.utils.functional import SimpleLazyObject

class UserFactory(factory.Factory):
    class Meta: 
        model = models.User


class ConferenceFactory(factory.Factory):
    class Meta:
        model = models.Conference


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
            username = 'Leo'
            )
        self.user2 = UserFactory()
        self.conference = ConferenceFactory(
            admin = self.user1
        )
        self.request1 = RequestFactory().post('./fake_path')
        self.request1.user = SimpleLazyObject(self.user1)
        self.request1.query_params = {}
        self.request2 = RequestFactory().post('./fake_path')
        self.request2.user = SimpleLazyObject(self.user2)
        self.request2.query_params = {}

    @skip('Test links are formed correctly')
    def test_get_links(self):
        pass

    @skip('Test submission count')
    def test_get_submission_count(self):
        pass

    def test_get_can_edit(self):
        self.serializer1 = ConferenceSerializer(context={'request': self.request1})
        self.serializer2 = ConferenceSerializer(context={'request': self.request2})
        self.canEdit1 = self.serializer1.get_can_edit(self.conference)
        self.canEdit2 = self.serializer2.get_can_edit(self.conference)
        self.assertTrue(self.canEdit1)
        self.assertTrue(self.canEdit2)


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
