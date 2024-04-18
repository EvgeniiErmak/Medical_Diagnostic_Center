# scripts/dump_authentication.py

from django.core.management import call_command
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Medical_Diagnostic_Center.settings')
django.setup()


def main():
    call_command('dumpdata', 'authentication.CustomUser', output='fixtures/authentication/authentication.json')


if __name__ == '__main__':
    main()
