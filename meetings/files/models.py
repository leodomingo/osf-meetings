from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    osf_id = models.UUIDField(editable=True)
    owner = models.ForeignKey(User)
    osf_path = models.URLField(blank=True)
