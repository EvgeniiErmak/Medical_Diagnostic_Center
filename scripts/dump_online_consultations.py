# scripts/dump_online_consultations.py

from django.core.management import call_command
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Medical_Diagnostic_Center.settings')
django.setup()


def main():
    call_command('dumpdata', 'online_consultations.Consultation',
                 'online_consultations.ConsultationSlot',
                 'online_consultations.ConsultationSession',
                 output='fixtures/online_consultations/online_consultations.json')


if __name__ == '__main__':
    main()
