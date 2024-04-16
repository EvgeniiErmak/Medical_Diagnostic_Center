# Medical_Diagnostic_Center/asgi.py

"""
ASGI config for Medical_Diagnostic_Center project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from online_consultations import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Medical_Diagnostic_Center.settings")

django_asgi_app = get_asgi_application()

websocket_urlpatterns = [
    path('ws/consultation/<int:consultation_id>/', consumers.ConsultationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/consultation/<int:consultation_id>/', consumers.ConsultationConsumer.as_asgi()),
        ])
    ),
})
