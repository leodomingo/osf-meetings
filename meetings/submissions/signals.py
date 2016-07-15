from django.contrib.auth.models import Group
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
from django.dispatch import receiver
from submissions.models import Submission
from django.db.models.signals import post_save
from guardian.shortcuts import assign_perm


@receiver(post_save, sender=Submission)
def add_permissions(sender, **kwargs):
    conference, created = kwargs["instance"], kwargs["created"]
    if created:
        # submission_contributor: get change, delete, view permissions
        assign_perm("submissions.change_submission", conference.admin, conference)
        assign_perm("submissions.delete_submission", conference.admin, conference)
        assign_perm("submissions.view_submission", conference.admin, conference)

        # current_osf_user: doesn't get any permissions initially
        current_osf_users = Group.objects.get(name=OsfOauth2AdapterConfig.osf_users_group)


        # public: gets only view permissions