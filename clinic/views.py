# clinic/views.py

from .models import Specialist, Service, Schedule
from django.shortcuts import render, get_object_or_404


def specialist_list(request):
    specialists = Specialist.objects.all()
    return render(request, 'clinic/specialist_list.html', {'specialists': specialists})


def specialist_schedule(request, specialist_id):
    specialist = get_object_or_404(Specialist, id=specialist_id)
    schedules = Schedule.objects.filter(specialist=specialist)
    return render(request, 'clinic/specialist_schedule.html', {'specialist': specialist, 'schedules': schedules})


def index(request):
    # Возвращает шаблон index.html
    return render(request, 'index.html')


def clinic_info(request):
    services = Service.objects.all()
    return render(request, 'clinic/clinic_info.html', {'services': services})


def specialist_detail(request, specialist_id):
    specialist = Specialist.objects.get(id=specialist_id)
    return render(request, 'clinic/specialist_detail.html', {'specialist': specialist})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def contacts(request):
    return render(request, 'contacts.html')
