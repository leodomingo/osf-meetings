from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from conferences.models import Conference


class Submission(models.Model):
    node_id = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    contributor = models.ForeignKey(User, blank=True, related_name="contributor")
    description = models.TextField()
    #conference = models.ForeignKey(Conference, related_name="conference", on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('date_created',)
