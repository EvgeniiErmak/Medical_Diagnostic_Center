# clinic/admin.py

from django.contrib import admin
from .models import Specialist, Service

admin.site.register(Specialist)
admin.site.register(Service)
