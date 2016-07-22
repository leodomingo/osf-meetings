from django.dispatch import receiver
from submissions.models import Submission
from django.db.models.signals import post_save
from submissions import permissions as perm
from approvals.permissions import (
    add_approval_permissions_to_submission_contributor,
    add_approval_permissions_to_conference_admin
)


@receiver(post_save, sender=Submission)
def add_permissions_on_submission_save(sender, **kwargs):
    submission = kwargs["instance"]
    approval = submission.approval
    conference_admin = submission.conference.admin
    submission_contributor = submission.contributor
    if submission.approval.approved:
        # public:
        perm.add_approved_submission_permissions_to_public(submission)

        # current_osf_user:
        perm.add_approved_submission_permissions_to_current_osf_user(
            submission)

        # submission_contributor:
        perm.add_submission_permissions_to_submission_contributor(
            submission, submission_contributor)
        add_approval_permissions_to_submission_contributor(
            approval, submission_contributor)

        # conference_admin:
        perm.add_submission_permissions_to_conference_admin(
            submission, conference_admin)
        add_approval_permissions_to_conference_admin(
            approval, conference_admin)

    else:
        # public:
        perm.remove_approved_submission_permissions_from_public(
            submission)

        # current_osf_user:
        perm.remove_approved_submission_permissions_from_current_osf_user(
            submission)

        # submission_contributor:
        perm.add_submission_permissions_to_submission_contributor(
            submission, submission_contributor)
        add_approval_permissions_to_submission_contributor(
            approval, submission_contributor)

        # conference_admin:
        perm.add_submission_permissions_to_conference_admin(
            submission, conference_admin)
        add_approval_permissions_to_conference_admin(
            approval, conference_admin)
