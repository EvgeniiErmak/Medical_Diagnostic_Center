# educational_resources/urls.py

from django.urls import path
from .views import resources_list, resource_detail

app_name = 'educational_resources'

urlpatterns = [
    path('', resources_list, name='resources_list'),
    path('<int:pk>/', resource_detail, name='resource_detail'),
]
