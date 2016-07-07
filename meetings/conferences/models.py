from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify


class Conference(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    site_url = models.URLField(blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    submission_start = models.DateTimeField(blank=True, null=True)
    submission_end = models.DateTimeField(blank=True, null=True)
    logo_url = models.URLField(blank=True)
    description = models.TextField(blank=True, max_length=500)

    def save(self, *args, **kwargs):
        self.id = slugify(self.title)
        super(Conference, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
