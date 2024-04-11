# feedback/forms.py

from django import forms
from .models import Feedback
import re


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'message']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        message = cleaned_data.get("message")

        # Список запрещенных слов
        banned_words = ['сука', 'блядь', 'хуй', 'пидарасы', 'мразь', 'ублюдки', 'ебанный', 'хуйло', 'и т.д.']

        # Проверка на наличие запрещенных слов в заголовке и сообщении
        for word in banned_words:
            if re.search(r'\b' + word + r'\b', title, re.IGNORECASE) or \
               re.search(r'\b' + word + r'\b', message, re.IGNORECASE):
                raise forms.ValidationError("Пожалуйста, избегайте использования нецензурной лексики в вашем отзыве.")

        return cleaned_data
