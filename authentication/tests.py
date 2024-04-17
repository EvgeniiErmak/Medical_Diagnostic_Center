# authentication/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm
from django.core import mail

User = get_user_model()


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com', password='password123', first_name='Test', is_active=True)
        self.inactive_user = User.objects.create_user(
            email='inactive@example.com', password='password123', first_name='Inactive', is_active=False)

    def test_user_registration(self):
        data = {
            'first_name': 'New',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = UserRegisterForm(data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('authentication:register'), data)
        self.assertEqual(response.status_code, 302)
        new_user = User.objects.get(email='newuser@example.com')
        # User should not be active until email confirmation
        self.assertFalse(new_user.is_active)
        self.assertEqual(len(mail.outbox), 1)  # Confirm an email has been sent

    def test_user_login(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.get(reverse('authentication:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_inactive_user_login(self):
        response = self.client.post(reverse('authentication:login'), {
                                    'username': 'inactive@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Your account is inactive.", response.content.decode())

    def test_logout(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.get(reverse('authentication:logout'))
        self.assertEqual(response.status_code, 302)

    def test_password_change(self):
        self.client.login(email='test@example.com', password='password123')
        response = self.client.post(reverse('authentication:password_change'), {
            'old_password': 'password123',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123'
        })
        self.assertTrue(
            response.context['user'].check_password('newpassword123'))
