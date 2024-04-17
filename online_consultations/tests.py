# online_consultations/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Consultation, ConsultationSlot
from clinic.models import Specialist
from django.utils import timezone
from channels.testing import WebsocketCommunicator
from .consumers import ConsultationConsumer
import json

User = get_user_model()


class OnlineConsultationsTestCase(TestCase):
    def setUp(self):
        # Создание тестового пользователя и специалиста
        self.user = User.objects.create_user(
            email='patient@example.com', password='testpassword')
        self.specialist = Specialist.objects.create(
            user=self.user, specialization='therapist', qualifications='None', experience_years=5)
        self.slot = ConsultationSlot.objects.create(
            specialist=self.specialist,
            start_time=timezone.now() + timezone.timedelta(days=1),
            end_time=timezone.now() + timezone.timedelta(days=1, hours=1),
            is_booked=False
        )
        self.consultation = Consultation.objects.create(
            patient=self.user,
            consultation_type='general',
            slot=self.slot
        )

    def test_consultation_str(self):
        self.assertIn("Consultation for", str(self.consultation))

    def test_book_consultation_view(self):
        self.client.login(email='patient@example.com', password='testpassword')
        response = self.client.post(reverse('online_consultations:book_consultation', args=[self.slot.id]), {
            'consultation_type': 'general',
            'issue': 'I need a consultation'
        })
        self.assertEqual(response.status_code, 302)

    def test_cancel_consultation_view(self):
        self.client.login(email='patient@example.com', password='testpassword')
        response = self.client.post(reverse(
            'online_consultations:cancel_consultation', args=[self.consultation.id]))
        self.assertEqual(response.status_code, 302)

    def test_consultation_detail_view(self):
        self.client.login(email='patient@example.com', password='testpassword')
        response = self.client.get(reverse(
            'online_consultations:consultation_detail', args=[self.consultation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Consultation for')

    def test_view_consultations(self):
        self.client.login(email='patient@example.com', password='testpassword')
        response = self.client.get(
            reverse('online_consultations:consultation_list'))
        self.assertEqual(response.status_code, 200)

    async def test_consultation_consumer(self):
        communicator = WebsocketCommunicator(
            ConsultationConsumer.as_asgi(
            ), f"/ws/consultation/{self.consultation.id}/"
        )
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        await communicator.send_to(text_data=json.dumps({'message': 'Hello'}))
        response = await communicator.receive_from()
        self.assertEqual(json.loads(response)['message'], 'Hello')
        await communicator.disconnect()
