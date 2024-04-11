# authentication/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['email', 'full_name', 'date_of_birth', 'gender', 'country', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active', 'gender', 'country']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'date_of_birth', 'gender', 'country', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name', 'date_of_birth', 'gender', 'country', 'address', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email',)


admin.site.register(CustomUser, UserAdmin)
