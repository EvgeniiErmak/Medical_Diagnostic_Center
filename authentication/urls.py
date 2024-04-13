# authentication/urls.py

from django.urls import path
from django.contrib.auth.views import PasswordResetCompleteView, PasswordChangeView
from .views import register, user_login, user_logout, dashboard, activate, CustomPasswordResetView, \
    CustomPasswordResetConfirmView, CustomPasswordChangeView

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',
         CustomPasswordResetView.as_view(template_name='authentication/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/',
         PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',
         PasswordChangeView.as_view(template_name='authentication/password_change_done.html'),
         name='password_change_done'),
]
