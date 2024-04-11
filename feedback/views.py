# feedback/views.py

from .models import Feedback, FAQ
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Проверяем наличие аналогичного отзыва от этого пользователя
            existing_feedback = Feedback.objects.filter(
                user=request.user,
                title=form.cleaned_data['title'],
                message=form.cleaned_data['message']
            )
            if existing_feedback.exists():
                # Если такой отзыв уже существует, информируем пользователя
                messages.error(request, 'Вы уже отправили аналогичный отзыв.')
            else:
                # Если аналогичного отзыва нет, сохраняем новый отзыв
                feedback = form.save(commit=False)
                feedback.user = request.user
                feedback.save()
                messages.success(request, 'Ваш отзыв успешно добавлен.')
                return redirect('feedback:feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})


def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'feedback/faq_list.html', {'faqs': faqs})
