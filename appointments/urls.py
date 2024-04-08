# appointments/urls.py

from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('list/', views.appointments_list, name='appointments_list'),
    path('book/<int:slot_id>/', views.book_appointment, name='book_appointment'),
    path('view/', views.view_appointments, name='view_appointments'),
]
