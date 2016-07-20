from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.

class Files(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    osf_id = models.UUIDField()
    url_file = models.URLField()
