# clinic/views.py

from django.shortcuts import render
from .models import Specialist, Service


def index(request):
    # Возвращает шаблон index.html
    return render(request, 'index.html')


def clinic_info(request):
    services = Service.objects.all()
    return render(request, 'clinic/clinic_info.html', {'services': services})


def specialist_detail(request, specialist_id):
    specialist = Specialist.objects.get(id=specialist_id)
    return render(request, 'clinic/specialist_detail.html', {'specialist': specialist})
