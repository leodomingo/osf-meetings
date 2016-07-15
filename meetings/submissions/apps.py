from __future__ import unicode_literals

from django.apps import AppConfig


class SubmissionAppConfig(AppConfig):
    name = 'submissions'

    def ready(self):
        import submissions.signals