# online_consultations/routing.py

from django.urls import re_path
from .consumers import ConsultationConsumer

websocket_urlpatterns = [
    re_path(r'ws/consultation/(?P<consultation_id>\d+)/$', ConsultationConsumer.as_asgi()),
]
