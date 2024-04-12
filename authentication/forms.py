# authentication/forms.py

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password1', 'password2', 'date_of_birth', 'gender', 'country', 'address']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
