# appointments/forms.py

from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    issue = forms.CharField(label='Вопрос', widget=forms.Textarea)

    class Meta:
        model = Appointment
        fields = ['issue']
