# clinic/models.py

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from datetime import date


class Equipment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image_url = models.URLField(verbose_name="URL изображения")
    description = models.TextField(verbose_name="Описание")
    specs = models.TextField(verbose_name="Технические характеристики")

    def __str__(self):
        return self.name


class Specialist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('пользователь'))
    age = models.PositiveIntegerField("Возраст", null=True, blank=True)
    specialization = models.CharField(
        max_length=100, verbose_name=_('специализация'))
    qualifications = models.TextField(verbose_name=_('квалификация'))
    experience_years = models.IntegerField(
        default=0, verbose_name=_('опыт работы'))
    education = models.TextField(blank=True, verbose_name=_('образование'))
    languages = models.CharField(
        max_length=100, blank=True, verbose_name=_('языки'))
    contact_email = models.EmailField(_('контактный email'), blank=True)
    contact_phone = models.CharField(
        _('контактный телефон'), max_length=20, blank=True)
    photo = models.ImageField(_('фотография специалиста'),
                              upload_to='specialists_photos/', null=True, blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return self.user.get_full_name()

    def calculate_age(self):
        if self.user.date_of_birth:
            today = date.today()
            return today.year - self.user.date_of_birth.year - (
                (today.month, today.day) < (self.user.date_of_birth.month, self.user.date_of_birth.day))
        return None  # Возвращаем None, если дата рождения не задана

    class Meta:
        verbose_name = _('специалист')
        verbose_name_plural = _('специалисты')


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    specialists = models.ManyToManyField(Specialist, related_name='services')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.IntegerField(_('day of the week'), choices=[(i, _(day)) for i, day in enumerate(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])])
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))

    def __str__(self):
        return f"{self.specialist} - {self.get_day_of_week_display()}"
