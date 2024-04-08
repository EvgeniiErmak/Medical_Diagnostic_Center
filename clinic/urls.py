# clinic/urls.py

from django.urls import path
from . import views

app_name = 'clinic'

urlpatterns = [
    path('info/', views.clinic_info, name='clinic_info'),
    path('specialist/<int:specialist_id>/', views.specialist_detail, name='specialist_detail'),
]
