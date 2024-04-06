# educational_resources/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.resources_list, name='resources_list'),
    path('<int:resource_id>/', views.resource_detail, name='resource_detail'),
]