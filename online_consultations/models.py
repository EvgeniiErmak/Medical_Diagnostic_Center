# online_consultations/models.py

from django.db import models
from django.conf import settings
from clinic.models import Specialist


class ConsultationSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='consultation_slots')
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.specialist}'s consultation slot from {self.start_time} to {self.end_time}"


class Consultation(models.Model):
    CONSULTATION_TYPES = (
        ('general', 'Общая консультация'),
        ('special', 'Специализированная консультация'),
        ('follow_up', 'Повторная консультация'),
        ('emergency', 'Экстренная консультация')
    )

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consultations')
    consultation_type = models.CharField(max_length=100, choices=CONSULTATION_TYPES, default='general')
    slot = models.OneToOneField(ConsultationSlot, on_delete=models.CASCADE, related_name='consultation', null=True)
    issue = models.TextField(default='Не оставил сообщение')

    def __str__(self):
        if self.slot and self.slot.specialist:
            return f"Consultation for {self.patient} with {self.slot.specialist} on {self.slot.start_time}"
        else:
            return f"Consultation for {self.patient} with no specialist"
