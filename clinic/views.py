# clinic/views.py

from django.shortcuts import render


def index(request):
    # Возвращает шаблон index.html
    return render(request, 'index.html')
