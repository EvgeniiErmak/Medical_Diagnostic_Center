# online_consultations/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
from clinic.models import Specialist


class Consultation(models.Model):
    # Определяем возможные типы консультаций
    CONSULTATION_TYPES = (
        ('general', 'Общая консультация'),
        ('special', 'Специализированная консультация'),
        ('follow_up', 'Повторная консультация'),
        ('emergency', 'Экстренная консультация')
    )

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consultations')
    specialist = models.ForeignKey(Specialist, on_delete=models.SET_NULL, null=True, related_name='consultations')
    consultation_type = models.CharField(max_length=100, choices=CONSULTATION_TYPES, default='general')
    consultation_date = models.DateTimeField(default=timezone.now)  # Прямое указание даты и времени
    issue = models.TextField(default='Не оставил сообщение')

    def __str__(self):
        if self.specialist:
            return f"Consultation for {self.patient} with {self.specialist} on {self.consultation_date.strftime('%Y-%m-%d %H:%M')}"
        else:
            return f"Consultation for {self.patient} with no specialist on {self.consultation_date.strftime('%Y-%m-%d %H:%M')}"
