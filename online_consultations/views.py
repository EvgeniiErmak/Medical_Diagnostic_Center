# online_consultations/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ConsultationForm
from .models import Consultation, Specialist  # Убедитесь, что импортируете Specialist правильно
from appointments.models import AppointmentSlot


@login_required
def schedule_consultation(request, specialist_id):  # Добавляем параметр specialist_id
    specialist = get_object_or_404(Specialist, pk=specialist_id)  # Получаем специалиста по ID
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = request.user  # Убедитесь, что используете patient вместо user
            consultation.specialist = specialist  # Присваиваем специалиста, если это необходимо
            consultation.save()
            # После сохранения консультации, помечаем слот как забронированный
            slot = get_object_or_404(AppointmentSlot, id=consultation.slot.id)
            slot.is_booked = True
            slot.save()
            messages.success(request, 'Вы успешно записаны на консультацию.')
            return redirect('online_consultations:consultation_list')
    else:
        form = ConsultationForm(initial={'specialist': specialist})
    return render(request, 'online_consultations/schedule_consultation.html', {
        'form': form,
        'specialist': specialist
    })


def consultation_list(request):
    consultations = Consultation.objects.filter(patient=request.user)
    return render(request, 'online_consultations/consultation_list.html', {'consultations': consultations})
