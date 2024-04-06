# clinic/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinic_info, name='clinic_info'),
    path('specialist/<int:specialist_id>/', views.specialist_detail, name='specialist_detail'),
]
