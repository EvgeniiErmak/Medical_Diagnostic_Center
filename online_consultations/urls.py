# online_consultations/urls.py

from django.urls import path
from . import views

app_name = 'online_consultations'

urlpatterns = [
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('schedule_consultation/<int:specialist_id>/', views.schedule_consultation, name='schedule_consultation'),
]
