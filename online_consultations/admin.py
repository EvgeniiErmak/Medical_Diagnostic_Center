# online_consultations/admin.py

from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Consultation, ConsultationSlot, ConsultationSession


class ConsultationSlotAdmin(admin.ModelAdmin):
    # Убедитесь, что эти атрибуты существуют
    list_display = ('specialist', 'start_time', 'end_time', 'is_booked')
    # Используйте корректные поля для фильтрации
    list_filter = ('is_booked', 'specialist__specialization')
    search_fields = ('specialist__user__first_name',
                     'specialist__user__last_name', 'start_time')


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'get_start_time', 'get_end_time', 'is_booked',
                    'consultation_type', 'issue', 'video_call_link')  # Добавлено video_call_link
    # Позволяет редактировать поле прямо в списке
    list_editable = ('video_call_link',)
    search_fields = ('patient__username', 'patient__first_name',
                     'patient__last_name', 'consultation_type')
    list_filter = ('consultation_type', 'slot__is_booked',
                   'slot__specialist__specialization')

    def get_start_time(self, obj):
        return obj.slot.start_time if obj.slot else "No slot assigned"
    get_start_time.admin_order_field = 'slot__start_time'
    get_start_time.short_description = _('Время начала')

    def get_end_time(self, obj):
        return obj.slot.end_time if obj.slot else "No slot assigned"
    get_end_time.admin_order_field = 'slot__end_time'
    get_end_time.short_description = _('Время окончания')

    def is_booked(self, obj):
        return obj.slot.is_booked if obj.slot else None
    is_booked.boolean = True
    is_booked.admin_order_field = 'slot__is_booked'
    is_booked.short_description = _('Забронирован')


admin.site.register(ConsultationSession)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(ConsultationSlot, ConsultationSlotAdmin)
