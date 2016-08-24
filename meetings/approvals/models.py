from __future__ import unicode_literals

from django.db import models


class Approval(models.Model):
    approved = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('view_approval', 'Can view approval'),
        )

    class JSONAPIMeta:
        resource_name = "approvals"
