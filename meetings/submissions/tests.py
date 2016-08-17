from django.test import TestCase
from unittest import skip
import factory
from datetime import datetime

from submissions.models import Submission
from conferences.tests import ConferenceFactory
from api.tests import UserFactory


class SubmissionFactory(factory.Factory):
    class Meta:
        model = Submission

    node_id = '12345'
    date_created = factory.LazyFunction(datetime.now)
    title = 'Even more'
    description = 'More text'
    conference = factory.SubFactory(ConferenceFactory)
    contributor = factory.SubFactory(UserFactory)


class TestPermissions(TestCase):
    @skip('Test different permissions in many test functions')
    def test_permissions(self):
        pass


class TestSerializers(TestCase):
    @skip('Test get_links, ensure that they are correct')
    def test_get_links(self):
        pass

    @skip('Test can edit, ensure it returns the correct permissions')
    def test_get_can_edit(self):
        pass


class TestSignals(TestCase):
    @skip('Test adding permissions via signal')
    def test_add_permissions_approved(self):
        pass

    @skip('Test adding permissions via signal')
    def test_add_permissions_rejected(self):
        pass


class TestViews(TestCase):
    @skip('Test create with many tests to cover')
    def test_create(self):
        pass

    @skip('Test queryset')
    def test_get_queryset(self):
        pass

    @skip('Relationship view, is this duplicating?')
    def test_relationship(self):
        pass
