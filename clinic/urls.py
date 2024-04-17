# clinic/urls.py

from django.urls import path
from .views import specialist_schedule, equipment_view
from . import views

app_name = 'clinic'

urlpatterns = [
    path('info/', views.clinic_info, name='clinic_info'),
    path('equipment/', views.equipment_view, name='equipment'),
    path('specialist/<int:specialist_id>/',
         views.specialist_detail, name='specialist_detail'),
    path('specialist/<int:specialist_id>/schedule/',
         specialist_schedule, name='specialist_schedule'),
    path('specialists/', views.specialist_list, name='specialist_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('contacts/', views.contacts, name='contacts'),
]
