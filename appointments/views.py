# appointments/views.py

from .models import AppointmentSlot, Appointment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required


@login_required
def appointments_list(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})


@login_required
def book_appointment(request, slot_id):  # Используем slot_id вместо specialist_id
    slot = get_object_or_404(AppointmentSlot, id=slot_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.slot = slot
            appointment.save()
            return redirect('appointments:view_appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form, 'slot': slot})


@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})
