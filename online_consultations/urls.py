# online_consultations/urls.py

from django.urls import path
from . import views

app_name = 'online_consultations'

urlpatterns = [
    path('list/', views.view_consultations, name='consultation_list'),
    path('book_consultation/<int:slot_id>/', views.book_consultation, name='book_consultation'),
    path('cancel/<int:consultation_id>/', views.cancel_consultation, name='cancel_consultation'),
    path('specialist/<int:specialist_id>/free_slots/', views.specialist_free_slots, name='specialist_free_slots'),
    path('schedule_consultation/<int:specialist_id>/', views.schedule_consultation, name='schedule_consultation'),
]
