# online_consultations/admin.py

from django.contrib import admin
from .models import Consultation
from django.utils.translation import gettext_lazy as _


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'datetime')  # Обновлено для соответствия полям модели
    list_filter = ('doctor', 'datetime')  # Обновлено для соответствия полям модели
    search_fields = ('user__username', 'doctor__user__first_name', 'doctor__user__last_name')  # Пример поисковых полей

    class Meta:
        verbose_name = _('консультация')
        verbose_name_plural = _('консультации')