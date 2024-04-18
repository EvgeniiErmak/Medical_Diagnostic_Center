# scripts/dump_appointments.py

from django.core.management import call_command
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Medical_Diagnostic_Center.settings')
django.setup()


def main():
    call_command('dumpdata', 'appointments.AppointmentSlot', 'appointments.Appointment',
                 output='fixtures/appointments/appointments.json')


if __name__ == '__main__':
    main()
