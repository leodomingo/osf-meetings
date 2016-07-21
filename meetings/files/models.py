from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    osf_id = models.UUIDField(default='')
    owner = models.ForeignKey(User)
    osf_file_link = models.URLField()
