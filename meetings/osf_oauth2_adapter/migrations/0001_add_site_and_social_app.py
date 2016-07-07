# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 18:24
from __future__ import unicode_literals

from django.db import migrations

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

CLIENT_ID = "c8afa24def0c47b6a261f6e431891d44"
CLIENT_SECRET = "9px3QS1DNcUNcnQEnW1RgnCutVoZcTDnFafnCIwO"

def make_social_app(apps, schema_editor):
	mysite = Site.objects.create(domain="osf.io", name="OSF")
	mysite.save()
	mysocialapp = SocialApp.objects.create(name="OSF", client_id=CLIENT_ID, secret=CLIENT_SECRET, key="", provider="osf")
	mysocialapp.sites.add(mysite)
	mysocialapp.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('socialaccount','0001_initial'),
    ]

    operations = [
    	migrations.RunPython(make_social_app),
    ]
