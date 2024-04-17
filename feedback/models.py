# feedback/models.py

from django.db import models
from django.conf import settings


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='feedbacks')
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_identifier = self.user.email
        return f"Feedback from {user_identifier}: {self.title}"


class FAQ(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return self.question
