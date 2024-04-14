# appointments/models.py

from django.db import models
from django.conf import settings
from clinic.models import Specialist


class AppointmentSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    specialist = models.ForeignKey('clinic.Specialist', on_delete=models.CASCADE, related_name='appointment_slots', default=2)  # предполагаем, что существует специалист с ID=1
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.specialist}'s slot from {self.start_time} to {self.end_time}"


class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    slot = models.OneToOneField(AppointmentSlot, on_delete=models.CASCADE, related_name='appointment')
    issue = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.slot.doctor} on {self.slot.start_time}"
