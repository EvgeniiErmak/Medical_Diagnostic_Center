# clinic/admin.py

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Specialist, Service, Schedule


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'experience_years')  # Показываем нужные поля
    search_fields = ('user__first_name', 'user__last_name', 'specialization')  # Поиск по имени и специализации
    list_filter = ('specialization', 'experience_years')  # Фильтры сбоку в админке

    def full_name(self, obj):
        return obj.user.get_full_name()  # Предполагаем, что у модели user есть метод get_full_name()

    full_name.short_description = _('Полное имя')  # Заголовок для колонки


admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Service)
admin.site.register(Schedule)
