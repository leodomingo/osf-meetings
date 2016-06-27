from django.contrib import admin

from .models import Node, SubmissionEval, Conference

admin.site.register(Node)
admin.site.register(SubmissionEval)
admin.site.register(Conference)
