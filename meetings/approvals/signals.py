from django.dispatch import receiver
from django.db.models.signals import post_save
from approvals.models import Approval


@receiver(post_save, sender=Approval)
def update_permissions_on_approval_save(sender, **kwargs):
    approval = kwargs["instance"]
    # cause submission signal to fire, updating permissions
    approval.submission.save()
