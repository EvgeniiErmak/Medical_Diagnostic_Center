# authentication/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'date_of_birth', 'gender', 'citizenship', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active', 'gender', 'citizenship']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'date_of_birth', 'gender', 'citizenship', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'date_of_birth', 'gender', 'citizenship', 'address', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name',)
    ordering = ('email',)


admin.site.register(CustomUser, UserAdmin)
