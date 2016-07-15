from django.contrib.auth.models import Group
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
from django.dispatch import receiver
from conferences.models import Conference
from django.db.models.signals import post_save
from guardian.shortcuts import assign_perm


@receiver(post_save, sender=Conference)
def add_permissions(sender, **kwargs):
    conference, created = kwargs["instance"], kwargs["created"]
    if created:
        # conference_admin: gets all permissions
        assign_perm("conferences.change_conference", conference.admin, conference)
        assign_perm("conferences.delete_conference", conference.admin, conference)

        # current_osf_user: gets only view permission
        # public: gets only view permissions