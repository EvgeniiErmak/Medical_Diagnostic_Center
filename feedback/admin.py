# feedback/admin.py

from django.contrib import admin
from .models import Feedback, FAQ

admin.site.register(Feedback)
admin.site.register(FAQ)
