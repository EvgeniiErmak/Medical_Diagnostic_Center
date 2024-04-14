# appointments/admin.py

from django.contrib import admin
from .models import Appointment, AppointmentSlot


class AppointmentSlotAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'start_time', 'end_time', 'is_booked')
    list_filter = ('is_booked', 'specialist')
    search_fields = ('specialist__user__first_name', 'specialist__user__last_name', 'start_time')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'get_start_time', 'get_end_time', 'is_booked')

    def get_start_time(self, obj):
        return obj.slot.start_time
    get_start_time.admin_order_field = 'slot__start_time'  # Позволяет сортировать по этому полю
    get_start_time.short_description = 'Время начала'  # Название колонки в админке

    def get_end_time(self, obj):
        return obj.slot.end_time
    get_end_time.admin_order_field = 'slot__end_time'  # Позволяет сортировать по этому полю
    get_end_time.short_description = 'Время окончания'  # Название колонки в админке

    def is_booked(self, obj):
        return obj.slot.is_booked
    is_booked.admin_order_field = 'slot__is_booked'
    is_booked.boolean = True  # Отображение в виде значка
    is_booked.short_description = 'Забронирован'


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(AppointmentSlot)  # Предположительно без изменений
