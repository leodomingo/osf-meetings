from django.dispatch import receiver
from django.db.models.signals import post_save
from approvals.models import Approval
from submissions.models import Submission

@receiver(post_save, sender=Approval)
def update_permissions_on_approval_save(sender, **kwargs):
    approval = kwargs["instance"]
    # cause submission signal to fire, updating permissions
    try:
    	approval.submission.save()
    except Submission.DoesNotExist, e:
    	# this needs to be logged somewhere
    	print('submission signal not triggered from approval signal') 