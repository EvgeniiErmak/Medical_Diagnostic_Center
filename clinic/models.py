# clinic/models.py

from django.conf import settings
from django.db import models


class Specialist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.specialization}"


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    specialists = models.ManyToManyField(Specialist, related_name='services')

    def __str__(self):
        return self.name
