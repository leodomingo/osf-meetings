from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from submissions.models import Submission
import uuid


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    osf_id = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User)
    osf_path = models.URLField(blank=True, null=True)
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
