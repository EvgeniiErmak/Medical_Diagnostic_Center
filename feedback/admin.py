# feedback/admin.py

from django.utils.translation import gettext_lazy as _
from .models import Feedback, FAQ
from django.contrib import admin


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['action_checkbox', 'title', 'user', 'created_at']  # Список полей, отображаемых в админке
    search_fields = ['title', 'message', 'user__username']  # Поля, по которым можно выполнять поиск
    list_filter = ['created_at', 'user']  # Фильтры сбоку в админке

    class Meta:
        verbose_name = _('обратная связь')
        verbose_name_plural = _('отзывы')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', )
