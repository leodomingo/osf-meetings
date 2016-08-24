from django.test import TestCase
from unittest import skip


class TestProvider(TestCase):

    @skip('Test OSF account to string')
    def test_to_string(self):
        pass

    @skip('Test extract common fields, mocking responses can be helpful')
    def test_extract_common_fields(self):
        pass

    @skip('Test extract uid, model mocked responses off of real responses')
    def test_extract_uid(self):
        pass

    @skip('Test get default scope')
    def test_get_default_scope(self):
        pass
