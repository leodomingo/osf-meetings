from __future__ import unicode_literals

from django.db import models
from submissions.models import Submission

from django_countries.fields import CountryField
from django.template.defaultfilters import slugify


class Conference(models.Model):
    id = models.SlugField(primary_key=True, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    site = models.URLField(blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    submission_start = models.DateTimeField()
    submission_end = models.DateTimeField()
    logo = models.URLField(blank=True)
    description = models.TextField(blank=True, max_length=500)

    class Meta:
        ordering = ('created',)
