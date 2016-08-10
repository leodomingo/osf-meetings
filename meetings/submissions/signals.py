from django.dispatch import receiver
from submissions.models import Submission
from django.db.models.signals import post_save
from submissions import permissions as perm


@receiver(post_save, sender=Submission)
def add_permissions_on_submission_save(sender, **kwargs):
    submission = kwargs["instance"]
    approval = submission.approval
    conference_admin = submission.conference.admin
    submission_contributor = submission.contributor

    if submission.approval.approved:
        perm.set_approved_submission_permissions(
            submission, submission_contributor, conference_admin, approval)

    else:
        perm.set_unapproved_submission_permissions(
            submission, submission_contributor, conference_admin, approval)
