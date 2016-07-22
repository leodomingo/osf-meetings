from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from conferences.models import Conference
import uuid


class Submission(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    node_id = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    #id for user - primary key
    contributor = models.ForeignKey(User, primary_key=True, related_name='submission_contributor')
    description = models.TextField()
    conference = models.ForeignKey(Conference)
    approval = models.OneToOneField('approvals.Approval', on_delete=models.CASCADE)
    file = models.OneToOneField('files.File', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_created',)
        permissions = (
            ('can_set_contributor', 'Can set the contributor for a submission'),
            ('view_submission', 'Can view submission'),
        )
