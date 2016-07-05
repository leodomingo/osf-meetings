from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from django.db import models

import datetime
from django_countries.fields import CountryField

# Create your models here.

class Submission(models.Model):
    node_id = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    contributors = models.ManyToManyField(User, blank=True)
    description = models.TextField()
    conference = models.ForeignKey('conferences.Conference')
    approved = models.NullBooleanField(blank=True)

    class Meta:
        ordering = ('date_created',)
