# online_consultations/admin.py

from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Consultation, ConsultationSlot


class ConsultationSlotAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'start_time', 'end_time', 'is_booked')
    list_filter = ('is_booked', 'specialist')
    search_fields = ('specialist__user__first_name', 'specialist__user__last_name', 'start_time')


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'get_start_time', 'get_end_time', 'is_booked', 'consultation_type', 'issue')

    def get_start_time(self, obj):
        if obj.slot:
            return obj.slot.start_time
        return "No slot assigned"
    get_start_time.admin_order_field = 'slot__start_time'
    get_start_time.short_description = _('Время начала')

    def get_end_time(self, obj):
        if obj.slot:
            return obj.slot.end_time
        return "No slot assigned"
    get_end_time.admin_order_field = 'slot__end_time'
    get_end_time.short_description = _('Время окончания')

    def is_booked(self, obj):
        if obj.slot:
            return obj.slot.is_booked
        return False
    is_booked.admin_order_field = 'slot__is_booked'
    is_booked.boolean = True
    is_booked.short_description = _('Забронирован')

    class Meta:
        verbose_name = _('консультация')
        verbose_name_plural = _('консультации')


admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(ConsultationSlot, ConsultationSlotAdmin)
