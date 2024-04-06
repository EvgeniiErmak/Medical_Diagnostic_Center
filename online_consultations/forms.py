# online_consultations/forms.py

from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['doctor', 'datetime']
