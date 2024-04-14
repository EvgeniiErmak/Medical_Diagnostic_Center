# appointments/urls.py

from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('list/', views.appointments_list, name='appointments_list'),
    path('book/<int:slot_id>/', views.book_appointment, name='book_appointment'),
    path('book/', views.book_appointment, name='book_appointment_by_query'),
    path('view/', views.view_appointments, name='view_appointments'),
    path('fetch_slots/', views.fetch_slots, name='fetch_slots'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('specialist/<int:specialist_id>/free_slots/', views.specialist_free_slots, name='specialist_free_slots'),
]
