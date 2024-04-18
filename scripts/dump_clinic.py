# scripts/dump_clinic.py

import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Medical_Diagnostic_Center.settings')
django.setup()


def main():
    # Указание файла для вывода и открытие его в режиме записи с использованием UTF-8
    with open('fixtures/clinic/clinic.json', 'w', encoding='utf-8') as output_file:
        call_command('dumpdata', 'clinic.Equipment', 'clinic.Specialist', 'clinic.Service', 'clinic.Schedule',
                     stdout=output_file, use_natural_foreign_keys=True, use_natural_primary_keys=True)


if __name__ == '__main__':
    main()
