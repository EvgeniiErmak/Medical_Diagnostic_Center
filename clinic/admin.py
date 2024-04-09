# clinic/admin.py

from django.contrib import admin
from .models import Specialist, Service, Schedule

admin.site.register(Specialist)
admin.site.register(Service)
admin.site.register(Schedule)
