from django.dispatch import receiver
from conferences.models import Conference
from django.db.models.signals import post_save
from conferences import permissions
from mail import mails


@receiver(post_save, sender=Conference)
def add_permissions(sender, **kwargs):
    conference, created = kwargs['instance'], kwargs['created']
    conference_admin = conference.admin
    if created:
        permissions.set_conference_permissions(conference, conference_admin)
        mails.create_mailgun_conference_route(conference.id, 'poster')
        mails.create_mailgun_conference_route(conference.id, 'talk')
