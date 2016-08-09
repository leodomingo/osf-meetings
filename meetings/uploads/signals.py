from django.dispatch import receiver
from uploads.models import Uoload
from django.db.models.signals import post_save
import permissions as perm


@receiver(post_save, sender=Upload)
def add_permissions_on_upload_save(sender, **kwargs):
    upload = kwargs["instance"]
    upload_owner = upload.owner
    perm.set_upload_permissions(upload, upload_owner)
