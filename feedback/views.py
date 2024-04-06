# feedback/views.py

from django.shortcuts import render, redirect
from .models import Feedback, FAQ
from .forms import FeedbackForm


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})


def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'feedback/faq_list.html', {'faqs': faqs})
