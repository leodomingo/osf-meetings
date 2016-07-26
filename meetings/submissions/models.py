from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from conferences.models import Conference


class Submission(models.Model):
    node_id = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    contributor = models.ForeignKey(User, related_name='submission_contributor')
    description = models.TextField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    approval = models.OneToOneField('approvals.Approval')

    class Meta:
        ordering = ('date_created',)
        permissions = (
            ('can_set_contributor', 'Can set the contributor for a submission'),
            ('view_submission', 'Can view submission'),
        )
