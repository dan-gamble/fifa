#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    settings = {
        'test': "fifa.settings.test",
        'dev': "fifa.settings.local"
    }

    if 'test' in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings['test'])
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings['dev'])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
