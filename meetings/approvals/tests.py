from django.test import TestCase
from unittest import skip
import factory

from approvals.signals import update_permissions_on_approval_save
from approvals.models import Approval
from submissions.tests import SubmissionFactory


class ApprovalFactory(factory.Factory):
    class Meta:
        model = Approval


class TestApprovals(TestCase):
    def setUp(self):
        self.sub = SubmissionFactory()

    def test_signal(self):
        update_permissions_on_approval_save()

    @skip('Test that permissions are limited, use as many defs as necessary')
    def test_permissions(self):
        pass
