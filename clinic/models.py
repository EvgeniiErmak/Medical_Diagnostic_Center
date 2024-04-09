# clinic/models.py

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Specialist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField()
    experience_years = models.IntegerField(default=0)
    education = models.TextField(blank=True)
    languages = models.CharField(max_length=100, blank=True)
    # Новые поля
    contact_email = models.EmailField(_('contact email'), blank=True)
    contact_phone = models.CharField(_('contact phone'), max_length=20, blank=True)
    photo = models.ImageField(_('profile photo'), upload_to='specialists_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    specialists = models.ManyToManyField(Specialist, related_name='services')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.IntegerField(_('day of the week'), choices=[(i, _(day)) for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])])
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))

    def __str__(self):
        return f"{self.specialist} - {self.get_day_of_week_display()}"
