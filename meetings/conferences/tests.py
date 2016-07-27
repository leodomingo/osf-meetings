from django.test import TestCase
from unittest import skip


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
