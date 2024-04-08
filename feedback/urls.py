# feedback/urls.py

from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('list/', views.feedback_list, name='feedback_list'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('faqs/', views.faq_list, name='faq_list'),
]
