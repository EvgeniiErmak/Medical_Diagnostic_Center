# online_consultations/admin.py

from django.contrib import admin
from .models import Consultation
from django.utils.translation import gettext_lazy as _


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'specialist', 'consultation_date', 'consultation_type', 'issue')
    list_filter = ('consultation_type', 'consultation_date', 'specialist')  # Фильтры для удобства поиска
    search_fields = ('patient__username', 'specialist__user__first_name', 'specialist__user__last_name', 'issue')  # Поля для поиска

    fieldsets = (
        (None, {
            'fields': ('patient', 'specialist', 'consultation_type', 'consultation_date', 'issue')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Сделать поля только для чтения при редактировании существующей записи
            return ['patient', 'specialist', 'consultation_type', 'issue']
        return []  # Нет полей только для чтения при создании новой записи

    class Meta:
        verbose_name = _('консультация')
        verbose_name_plural = _('консультации')
