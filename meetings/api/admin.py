from django.contrib import admin

from .models import Submission, Meeting

admin.site.register(Submission)
admin.site.register(Meeting)