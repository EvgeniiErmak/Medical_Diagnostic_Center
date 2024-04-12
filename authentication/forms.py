# authentication/forms.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(required=True, label='ФИО')
    email = forms.EmailField(required=True, label='Электронная почта')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'last_name', 'first_name', 'middle_name',
            'date_of_birth', 'age', 'gender',
            'citizenship', 'residence'
        ]
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'middle_name': 'Отчество',
            'date_of_birth': 'Дата рождения',
            'age': 'Возраст',
            'gender': 'Пол',
            'citizenship': 'Гражданство',
            'residence': 'Место жительства'
        }
