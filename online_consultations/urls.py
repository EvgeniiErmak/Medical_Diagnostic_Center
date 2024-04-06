# online_consultations/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('schedule_consultation/', views.schedule_consultation, name='schedule_consultation'),
]
