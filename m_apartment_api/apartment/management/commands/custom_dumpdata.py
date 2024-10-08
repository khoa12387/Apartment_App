import sys

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import Group, Permission
import codecs
from apartment.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        output_filename = 'data.json'

        with codecs.open(output_filename, 'w', 'utf-8') as f:
            original_stdout = sys.stdout
            sys.stdout = f

            app_name = 'apartment'

            # models = [Group, Permission]

            from django.apps import apps
            # models = apps.get_app_config(app_name).get_models()
            app_models = list(apps.get_app_config('apartment').get_models())
            models = app_models + [Group]

            for model in models:
                call_command('dumpdata', model._meta.label, indent=4,
                             use_natural_foreign_keys=True, use_natural_primary_keys=True)

            sys.stdout = original_stdout