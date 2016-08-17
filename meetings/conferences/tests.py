from django.test import TestCase
from unittest import skip
import factory
from datetime import datetime

from conferences.models import Conference


class ConferenceFactory(factory.Factory):
    class Meta:
        model = Conference

    id = 'abc123'
    created = factory.LazyFunction(datetime.now)
    modified = factory.LazyFunction(datetime.now)
    title = 'This is a conference'
    city = factory.Iterator(['Cville', 'Denver'])
    state = factory.Iterator(['WY', 'HI', 'VA'])


class TestPermissions(TestCase):
    @skip('use several tests to test different permissions aspects')
    def test_conference_creator(self):
        pass


class TestSerializers(TestCase):
    @skip('Test links are formed correctly')
    def test_get_links(self):
        pass

    @skip('Test submission count')
    def test_get_submission_count(self):
        pass

    @skip('Test can_edit, use multiple tests')
    def test_get_can_edit(self):
        pass


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
