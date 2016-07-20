from django.contrib.auth.models import Group
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig
from django.dispatch import receiver
from conferences.models import Conference
from django.db.models.signals import post_save
from guardian.shortcuts import assign_perm
from conferences import permissions


@receiver(post_save, sender=Conference)
def add_permissions(sender, **kwargs):
    conference, created = kwargs["instance"], kwargs["created"]
    conference_admin = conference.admin
    if created:
        # conference_admin:
        permissions.add_conference_permissions_to_conference_admin(
            conference, conference_admin)

        # current_osf_user:
        permissions.add_conference_permissions_to_current_osf_user(conference)

        # public:
        permissions.add_conference_permissions_to_public(conference)
