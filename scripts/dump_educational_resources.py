# scripts/dump_educational_resources.py

from django.core.management import call_command
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Medical_Diagnostic_Center.settings')
django.setup()


def main():
    call_command('dumpdata', 'educational_resources.Resource',
                 output='fixtures/educational_resources/educational_resources.json')


if __name__ == '__main__':
    main()
