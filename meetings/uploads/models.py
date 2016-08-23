from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Upload(models.Model):
    owner = models.ForeignKey(User, related_name='upload_owner')
    date_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True, default='')

    class Meta:
        permissions = (
            ('view_upload', 'Can view upload'),
        )

    class JSONAPIMeta:
        resource_name = "uploads"
