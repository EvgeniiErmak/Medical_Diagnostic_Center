# online_consultations/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Consultation, ConsultationSlot
from clinic.models import Specialist
from .forms import ConsultationForm
from django.contrib import messages
from django.utils import timezone
from .models import ConsultationSession
from django.http import JsonResponse


@login_required
def consultation_detail(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    return render(request, 'online_consultations/consultation_detail.html', {'consultation': consultation})


def create_offer(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    # Предполагаемая логика для создания WebRTC оффера
    offer = "create WebRTC offer logic here"
    ConsultationSession.objects.create(consultation=consultation, offer=offer)
    return JsonResponse({'offer': offer})


def receive_answer(request, session_id):
    session = get_object_or_404(ConsultationSession, id=session_id)
    answer = request.POST.get('answer')
    session.answer = answer
    session.save()
    return JsonResponse({'status': 'answer received'})


@login_required
def book_consultation(request, slot_id):
    slot = get_object_or_404(ConsultationSlot, id=slot_id, is_booked=False)
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            if not slot.is_booked:
                consultation = form.save(commit=False)
                consultation.patient = request.user
                consultation.slot = slot
                consultation.save()
                slot.is_booked = True
                slot.save()
                messages.success(request, 'Вы успешно записаны на консультацию.')
                return redirect('online_consultations:consultation_list')
            else:
                messages.error(request, 'Этот слот уже забронирован.')
        else:
            messages.error(request, 'Произошла ошибка при обработке формы.')
    else:
        form = ConsultationForm()

    return render(request, 'online_consultations/book_consultation.html', {'form': form, 'slot': slot})


@login_required
def view_consultations(request):
    consultations = Consultation.objects.filter(patient=request.user).select_related('slot')
    return render(request, 'online_consultations/consultation_list.html', {'consultations': consultations})


@login_required
def cancel_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id, patient=request.user)
    if consultation:
        if timezone.now() < consultation.slot.start_time:
            slot = consultation.slot
            slot.is_booked = False
            slot.save()
            consultation.delete()
            messages.success(request, 'Ваша консультация была успешно отменена.')
        else:
            messages.error(request, 'Отмена консультации невозможна, так как указанное время уже прошло.')
    else:
        messages.error(request, 'Не удалось найти консультацию для отмены.')
    return redirect('online_consultations:consultation_list')


@login_required
def specialist_free_slots(request, specialist_id):
    specialist = get_object_or_404(Specialist, pk=specialist_id)
    free_slots = ConsultationSlot.objects.filter(specialist=specialist, is_booked=False)
    return render(request, 'online_consultations/specialist_free_slots.html', {
        'specialist': specialist,
        'free_slots': free_slots
    })


def schedule_consultation(request, specialist_id):
    # Убедитесь, что Specialist импортирован и используется корректно
    specialist = get_object_or_404(Specialist, pk=specialist_id)
    # Логика обработки запроса
    return render(request, 'online_consultations/schedule_consultation.html', {'specialist': specialist})
