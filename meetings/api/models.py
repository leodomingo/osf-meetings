from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
import datetime
from django_countries.fields import CountryField
from django.db import models

# Create your models here.

class Submission(models.Model):
    osf_id = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    contributors = models.ForeignKey(Group)
    description = models.TextField()
    conference = models.ForeignKey('conference')

    class Meta:
        ordering = ('date_created',)

class Conference(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    site_url = models.URLField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    submission_start = models.DateTimeField()
    submission_end = models.DateTimeField()
    logo_url = models.URLField()
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ('created',)
