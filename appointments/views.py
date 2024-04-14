# appointments/views.py

from clinic.models import Specialist
from .models import AppointmentSlot, Appointment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppointmentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)
    if appointment:
        # Проверяем, не прошло ли уже время слота
        if timezone.now() < appointment.slot.start_time:
            slot = appointment.slot
            slot.is_booked = False
            slot.save()
            appointment.delete()
            messages.success(request, 'Ваша запись на прием была успешно отменена.')
        else:
            messages.error(request, 'Отмена записи невозможна, так как указанное время уже прошло.')
    else:
        messages.error(request, 'Не удалось найти запись на прием для отмены.')
    return redirect('appointments:appointments_list')


@login_required
def fetch_slots(request):
    """ Fetch available slots and return them in JSON format for FullCalendar. """
    slots = AppointmentSlot.objects.filter(is_booked=False)
    slots_data = [{'id': slot.id, 'start_time': slot.start_time.isoformat(), 'end_time': slot.end_time.isoformat()} for slot in slots]
    return JsonResponse(slots_data, safe=False)


@login_required
def appointments_list(request):
    """ Display a list of appointments for the logged-in user. """
    appointments = Appointment.objects.filter(patient=request.user).select_related('slot')
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})


@login_required
def book_appointment(request, slot_id):
    """ Handle booking an appointment for a given slot. """
    slot = get_object_or_404(AppointmentSlot, id=slot_id, is_booked=False)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            if not slot.is_booked:  # Additional check to prevent race conditions
                appointment = form.save(commit=False)
                appointment.patient = request.user
                appointment.slot = slot
                appointment.save()
                slot.is_booked = True  # Mark the slot as booked
                slot.save()
                messages.success(request, 'Вы успешно записаны на прием.')
                return redirect('appointments:view_appointments')
            else:
                messages.error(request, 'Этот слот уже забронирован.')
        else:
            messages.error(request, 'Произошла ошибка при обработке формы.')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form, 'slot': slot})


@login_required
def view_appointments(request):
    """ Display all appointments for the logged-in user. """
    appointments = Appointment.objects.filter(patient=request.user).select_related('slot')
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})


@login_required
def specialist_free_slots(request, specialist_id):
    specialist = get_object_or_404(Specialist, pk=specialist_id)
    free_slots = AppointmentSlot.objects.filter(specialist=specialist, is_booked=False)
    return render(request, 'appointments/specialist_free_slots.html', {'specialist': specialist, 'free_slots': free_slots})
