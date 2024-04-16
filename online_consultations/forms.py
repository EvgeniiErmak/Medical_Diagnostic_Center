# online_consultations/forms.py

from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['consultation_type', 'issue']

    def __init__(self, *args, **kwargs):
        super(ConsultationForm, self).__init__(*args, **kwargs)
        self.fields['consultation_type'].label = "Тип консультации"
        self.fields['issue'].label = "Описание проблемы"
