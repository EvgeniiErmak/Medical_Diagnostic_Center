# authentication/urls.py

from django.urls import path
from .views import register, user_login, user_logout, dashboard, activate

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
