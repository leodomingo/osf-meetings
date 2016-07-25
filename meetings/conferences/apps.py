from __future__ import unicode_literals

from django.apps import AppConfig


class ConferenceAppConfig(AppConfig):
    name = 'conferences'

    def ready(self):
        import conferences.signals #noqa
