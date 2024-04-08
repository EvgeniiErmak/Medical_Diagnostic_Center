# appointments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AppointmentSlot, Appointment
from .forms import AppointmentForm


def appointments_list(request):
    # Замените 'user' на 'patient', чтобы отфильтровать записи по текущему пользователю
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})


@login_required
def book_appointment(request, slot_id):
    slot = AppointmentSlot.objects.get(id=slot_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.slot = slot
            appointment.save()
            slot.is_booked = True
            slot.save()
            return redirect('appointments:view_appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form, 'slot': slot})


@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})
