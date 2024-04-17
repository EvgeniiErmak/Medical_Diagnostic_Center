# clinic/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Equipment, Specialist, Service, Schedule
from django.contrib.auth import get_user_model
from datetime import date, time

User = get_user_model()


class ClinicTestCase(TestCase):
    def setUp(self):
        # Создание пользователя для связи со специалистом
        self.user = User.objects.create_user(email='specialist@example.com', password='password123', first_name='John',
                                             last_name='Doe', date_of_birth=date(1985, 5, 15))

        # Создание специалиста
        self.specialist = Specialist.objects.create(
            user=self.user,
            age=36,
            specialization='Cardiology',
            qualifications='Extensive experience in complex cardiological cases.',
            experience_years=10,
            education='Medical University',
            languages='English, Spanish',
            contact_email='specialist@example.com',
            contact_phone='123-456-7890'
        )

        # Создание оборудования
        self.equipment = Equipment.objects.create(
            name='Ultrasound Machine',
            image_url='http://example.com/image.jpg',
            description='Used for ultrasound imaging.',
            specs='Specs detail here'
        )

        # Создание сервиса и связывание его со специалистом
        self.service = Service.objects.create(name='Cardiology Consultation',
                                              description='Detailed cardiology consulting services.')
        self.service.specialists.add(self.specialist)

        # Создание расписания для специалиста
        self.schedule = Schedule.objects.create(
            specialist=self.specialist,
            day_of_week=1,  # Понедельник
            start_time=time(9, 0),
            end_time=time(17, 0)
        )

    def test_specialist_full_name(self):
        self.assertEqual(self.specialist.full_name(), 'John Doe')

    def test_specialist_age_calculation(self):
        calculated_age = self.specialist.calculate_age()
        expected_age = date.today().year - 1985 - \
            ((date.today().month, date.today().day) < (5, 15))
        self.assertEqual(calculated_age, expected_age)

    def test_equipment_str(self):
        self.assertEqual(str(self.equipment), 'Ultrasound Machine')

    def test_specialist_schedule_str(self):
        day = self.schedule.get_day_of_week_display()
        # Проверка строкового представления
        self.assertIn('Monday', str(self.schedule))

    def test_specialist_list_view(self):
        response = self.client.get(reverse('clinic:specialist_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('specialists', response.context)
        self.assertEqual(len(response.context['specialists']), 1)

    def test_equipment_view(self):
        response = self.client.get(reverse('clinic:equipment'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ultrasound Machine')

    def test_specialist_detail_view(self):
        response = self.client.get(
            reverse('clinic:specialist_detail', args=[self.specialist.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_clinic_info_view(self):
        response = self.client.get(reverse('clinic:clinic_info'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cardiology Consultation')
