from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
import datetime

from django.db import models

# Create your models here.

class Submission(models.Model):
	node_id = models.CharField(max_length=10)
	date_created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	contributors = models.ManyToManyField(User, blank=True)
	description = models.TextField()
	conference = models.ForeignKey('conference')
	approved = models.NullBooleanField(blank=True)

	class Meta:
		ordering = ('date_created',)

class Conference(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	submission_date = models.DateField(null=True)
	close_date = models.DateField(null=True)
	logo_url = models.CharField(max_length=500)
	tags = models.CharField(max_length=500) # change to ManyToManyField(Tag)
	sponsors = models.CharField(max_length=500)
	description = models.TextField()

	class Meta:
		ordering = ('created',)
