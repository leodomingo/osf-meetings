from rest_framework import serializers as ser
from django_countries.fields import CountryField

from conferences.models import Conference

class ConferenceSerializer(ser.ModelSerializer):
    country = CountryField() #get country_dict working later
    start = ser.DateTimeField(source='event_start')
    end = ser.DateTimeField(source='event_end')
    submissionstart = ser.DateTimeField(source='submission_start')
    submissionend = ser.DateTimeField(source='submission_end')
    site = ser.URLField(required=False, allow_blank=True)
    #url for now
    logo = ser.URLField(required=False, allow_blank=True)

    # Later on add tags and sponsors back
    class Meta:
        model = Conference

        fields = ('created', 'modified', 'id', 'title', 'logo', 'site', 'city',
                'state', 'country', 'start', 'end', 'submissionstart', 
                'submissionend', 'description')
