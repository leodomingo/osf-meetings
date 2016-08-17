from django.test import TestCase
from unittest import skip
import factory
import mock

from approvals.signals import update_permissions_on_approval_save
from approvals.models import Approval
from submissions.tests import SubmissionFactory


class ApprovalFactory(factory.Factory):
    class Meta:
        model = Approval


class TestApprovals(TestCase):
    def setUp(self):
        self.approval = ApprovalFactory(id=1)
        self.sub = SubmissionFactory(approval=self.approval)

    def test_signal(self, mock_signal):
        self.approval.save()

    @skip('Test that permissions are limited, use as many defs as necessary')
    def test_permissions(self):
        pass
