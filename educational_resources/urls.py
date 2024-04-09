# educational_resources/urls.py

from django.urls import path
from . import views

app_name = 'educational_resources'

urlpatterns = [
    path('resources/', views.resources_list, name='resources_list'),
    path('resources/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resources/1/', views.resource_detail_1, name='resource_detail_1'),
    path('resources/2/', views.resource_detail_2, name='resource_detail_2'),
    path('resources/3/', views.resource_detail_3, name='resource_detail_3'),
    path('resources/4/', views.resource_detail_4, name='resource_detail_4'),
    path('resources/5/', views.resource_detail_5, name='resource_detail_5'),
]
