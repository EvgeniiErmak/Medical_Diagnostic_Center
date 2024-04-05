# appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:slot_id>/', views.book_appointment, name='book_appointment'),
    path('view/', views.view_appointments, name='view_appointments'),
]
