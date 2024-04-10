# educational_resources/admin.py

from django.contrib import admin
from .models import Resource
from django_summernote.widgets import SummernoteWidget
from django import forms


# Определяем админ-форму для модели Resource
class ResourceAdminForm(forms.ModelForm):
    # Используем SummernoteWidget для поля content
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Resource
        fields = '__all__'


# Определяем админ-класс для модели Resource
class ResourceAdmin(admin.ModelAdmin):
    form = ResourceAdminForm


# Регистрируем модель Resource с использованием определенного админ-класса
admin.site.register(Resource, ResourceAdmin)
