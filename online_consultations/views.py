# online_consultations/views.py

from django.shortcuts import render, redirect
from .models import Consultation
from .forms import ConsultationForm


def consultation_list(request):
    consultations = Consultation.objects.filter(user=request.user)
    return render(request, 'online_consultations/consultation_list.html', {'consultations': consultations})


def schedule_consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'online_consultations/schedule_consultation.html', {'form': form})
