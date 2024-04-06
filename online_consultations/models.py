# online_consultations/models.py

from django.db import models
from django.conf import settings


class Consultation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey('clinic.Specialist', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Consultation with {self.doctor} at {self.datetime}"
