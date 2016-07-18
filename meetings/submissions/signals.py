from django.contrib.auth.models import Group, User
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
from django.dispatch import receiver
from submissions.models import Submission
from django.db.models.signals import post_save
from guardian.shortcuts import assign_perm, remove_perm


@receiver(post_save, sender=Submission)
def add_permissions_on_submission_save(sender, **kwargs):
    submission = kwargs["instance"]
    current_osf_users = Group.objects.get(name=OsfOauth2AdapterConfig.osf_users_group)
    public = User.objects.get(username="AnonymousUser")
    conference_admin = submission.conference.admin
    if submission.approved:
        # public:
        assign_perm("submissions.view_submission", public, submission)

        # current_osf_user:
        assign_perm("submissions.view_submission", current_osf_users, submission)
        print(current_osf_users.user_set.all())

        # submission_contributor:
        assign_perm("submissions.change_submission", submission.contributor, submission)
        assign_perm("submissions.delete_submission", submission.contributor, submission)
        assign_perm("submissions.view_submission", submission.contributor, submission)

        # conference_admin:
        assign_perm("submissions.change_submission", conference_admin, submission)
        assign_perm("submissions.delete_submission", conference_admin, submission)
        assign_perm("submissions.view_submission", conference_admin, submission)

    else:
        # public:
        remove_perm("submissions.view_submission", public, submission)

        # current_osf_user:
        remove_perm("submissions.view_submission", current_osf_users, submission)

        # submission_contributor:
        assign_perm("submissions.change_submission", submission.contributor, submission)
        assign_perm("submissions.delete_submission", submission.contributor, submission)
        assign_perm("submissions.view_submission", submission.contributor, submission)

       # conference_admin:
        assign_perm("submissions.change_submission", conference_admin, submission)
        assign_perm("submissions.delete_submission", conference_admin, submission)
        assign_perm("submissions.view_submission", conference_admin, submission)

