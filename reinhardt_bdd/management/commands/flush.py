from django.conf import settings
from django.core.management.commands.flush import Command as BaseFlushCommand


class Command(BaseFlushCommand):
    def handle(self, **options):
        if settings.FIX_WAGTAIL_FLUSH:
            options['allow_cascade'] = True
        super(Command, self).handle(**options)
