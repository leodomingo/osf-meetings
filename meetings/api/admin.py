from django.contrib import admin
from .models import Submission, Conference, Tag

admin.site.register(Submission)
admin.site.register(Conference)
admin.site.register(Tag)