# authentication/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'date_of_birth', 'gender', 'citizenship', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active', 'gender', 'citizenship']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'date_of_birth', 'gender', 'citizenship', 'residence')}),
        (_('Разрешения'), {'fields': ('is_staff', 'is_active')}),
        (_('Важные даты'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'date_of_birth', 'gender', 'citizenship', 'residence', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name',)
    ordering = ('email',)

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')


admin.site.register(CustomUser, UserAdmin)
