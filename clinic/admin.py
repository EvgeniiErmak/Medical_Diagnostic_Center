# clinic/admin.py

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Specialist, Service, Schedule
from datetime import date
from .models import Equipment


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'get_age', 'specialization', 'experience_years')  # Отображаем поля в админке
    search_fields = ('user__first_name', 'user__last_name', 'specialization')  # Поиск по имени и специализации
    list_filter = ('specialization', 'experience_years')  # Фильтры сбоку в админке

    def full_name(self, obj):
        return obj.user.get_full_name()  # Предполагаем, что у модели user есть метод get_full_name()
    full_name.short_description = _('Полное имя')  # Заголовок для колонки

    def get_age(self, obj):
        # Расчет возраста специалиста, если дата рождения задана
        if obj.user.date_of_birth:
            today = date.today()
            return today.year - obj.user.date_of_birth.year - ((today.month, today.day) < (obj.user.date_of_birth.month, obj.user.date_of_birth.day))
        return _("Дата рождения не указана")
    get_age.short_description = _('Возраст')  # Заголовок для колонки возраста


# Регистрируем модели в админ-панели
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Equipment)
