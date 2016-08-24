from django.test import TestCase
from unittest import skip
import mock

from approvals.signals import update_permissions_on_approval_save
import test_factories


class TestApprovals(TestCase):
    def setUp(self):
        self.approval = test_factories.ApprovalFactory(id=1)
        self.sub = test_factories.SubmissionFactory(approval=self.approval)

    def test_signal(self, mock_signal):
        self.approval.save()

    @skip('Test that permissions are limited, use as many defs as necessary')
    def test_permissions(self):
        pass
