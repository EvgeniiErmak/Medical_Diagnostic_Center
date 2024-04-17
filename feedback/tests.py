# feedback/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Feedback, FAQ
from .forms import FeedbackForm
from django.contrib.messages import get_messages

User = get_user_model()

class FeedbackTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='testpassword123')
        self.client.login(email='user@example.com', password='testpassword123')

    def test_feedback_submission_valid(self):
        response = self.client.post(reverse('feedback:submit_feedback'), {
            'title': 'Great Service',
            'message': 'I had a wonderful experience!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Feedback.objects.exists())

    def test_feedback_submission_duplicate(self):
        Feedback.objects.create(user=self.user, title='Duplicate', message='This is a duplicate message.')
        response = self.client.post(reverse('feedback:submit_feedback'), {
            'title': 'Duplicate',
            'message': 'This is a duplicate message.'
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Вы уже отправили аналогичный отзыв.')

    def test_feedback_form_profanity(self):
        form_data = {
            'title': 'Terrible service',
            'message': 'This was абсолютно ужасно, блядь!'
        }
        form = FeedbackForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'][0], 'Пожалуйста, избегайте использования нецензурной лексики в вашем отзыве.')

    def test_faq_list_view(self):
        FAQ.objects.create(question='What is your return policy?', answer='You can return products within 30 days.')
        response = self.client.get(reverse('feedback:faq_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is your return policy?')

    def test_feedback_list_view(self):
        Feedback.objects.create(user=self.user, title='Feedback', message='Just a feedback.')
        response = self.client.get(reverse('feedback:feedback_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Just a feedback.')
