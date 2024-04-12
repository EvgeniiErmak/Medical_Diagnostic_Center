# authentication/views.py

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('authentication:dashboard')  # Перенаправление на панель пользователя после регистрации
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('authentication:dashboard')  # Перенаправление на панель пользователя после входа
    else:
        form = UserLoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')  # Перенаправление на главную страницу после выхода


def dashboard(request):
    # Предполагаем, что у модели пользователя есть поля для медицинских данных
    if not request.user.is_authenticated:
        return redirect('authentication:login')
    return render(request, 'authentication/dashboard.html', {
        'user': request.user
    })
