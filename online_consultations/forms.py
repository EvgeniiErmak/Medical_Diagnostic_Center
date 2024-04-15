# online_consultations/forms.py

from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient', 'specialist', 'consultation_type', 'consultation_date', 'issue']
        widgets = {
            'consultation_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'patient': 'Пациент',
            'specialist': 'Специалист',
            'consultation_type': 'Тип консультации',
            'consultation_date': 'Дата и время консультации',
            'issue': 'Описание проблемы'
        }
