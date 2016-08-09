from __future__ import unicode_literals

from django.apps import AppConfig


class UploadsConfig(AppConfig):
    name = 'uploads'

    def ready(self):
        import submissions.signals  # noqa
