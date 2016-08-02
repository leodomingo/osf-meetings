from django.test import TestCase
from unittest import skip


class TestApprovals(TestCase):
    @skip('Make sure a signal actually saves the object')
    def test_signal(self):
        pass

    @skip('Test that permissions are limited, use as many defs as necessary')
    def test_permissions(self):
        pass
