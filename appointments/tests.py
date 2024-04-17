# appointments/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import AppointmentSlot, Appointment
from clinic.models import Specialist
from .forms import AppointmentForm
from django.urls import reverse
import json

User = get_user_model()


class AppointmentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345', email='test@example.com')
        self.specialist = Specialist.objects.create(
            name='Dr. Good', title='Dermatologist')
        self.slot = AppointmentSlot.objects.create(
            start_time=timezone.now() + timezone.timedelta(days=1),
            end_time=timezone.now() + timezone.timedelta(days=1, hours=1),
            specialist=self.specialist,
            is_booked=False
        )
        self.appointment = Appointment.objects.create(
            patient=self.user,
            slot=self.slot,
            issue='Routine checkup'
        )

    def test_models(self):
        self.assertEqual(self.slot.is_booked, False)
        self.assertIn('Routine checkup', self.appointment.issue)

    def test_appointment_form(self):
        form_data = {'issue': 'Updated issue'}
        form = AppointmentForm(data=form_data, instance=self.appointment)
        self.assertTrue(form.is_valid())
        appointment = form.save()
        self.assertEqual(appointment.issue, 'Updated issue')

    def test_book_appointment_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('appointments:book_appointment', args=[self.slot.id]), {
            'issue': 'Routine checkup'
        })
        self.assertEqual(response.status_code, 302)
        updated_slot = AppointmentSlot.objects.get(id=self.slot.id)
        self.assertTrue(updated_slot.is_booked)

    def test_cancel_appointment_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(
            reverse('appointments:cancel_appointment', args=[self.appointment.id]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Appointment.DoesNotExist):
            Appointment.objects.get(id=self.appointment.id)

    def test_fetch_slots_view(self):
        response = self.client.get(reverse('appointments:fetch_slots'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_view_appointments_list(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('appointments:appointments_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'appointments/appointments_list.html')
        self.assertIn('appointments', response.context)
