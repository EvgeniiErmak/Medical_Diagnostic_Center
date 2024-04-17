# authentication/views.py

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from .forms import UserRegisterForm, UserLoginForm, CustomPasswordChangeForm, UserProfileForm
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_str, force_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from .models import CustomUser


account_activation_token = PasswordResetTokenGenerator()


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Ваш аккаунт был успешно активирован!')
        return redirect('authentication:dashboard')
    else:
        return render(request, 'authentication/activation_invalid.html')


def send_activation_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    activation_link = request.build_absolute_uri(
        reverse('authentication:activate', kwargs={
                'uidb64': uid, 'token': token})
    )
    subject = 'Активация аккаунта'
    message = f'Здравствуйте, {user.first_name}! Пожалуйста, активируйте свой аккаунт, перейдя по следующей ссылке: {activation_link}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Пользователь не активен до подтверждения по email
            user.save()
            # Отправка письма для активации
            send_activation_email(user, request)
            messages.info(
                request, 'Пожалуйста, подтвердите вашу регистрацию, проверив указанную электронную почту.')
            return redirect('authentication:login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me', False)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    # Session will expire in 30 days
                    request.session.set_expiry(
                        30 * 24 * 60 * 60)  # 30 days in seconds
                else:
                    # Session will expire when the user closes the browser
                    request.session.set_expiry(0)
                return redirect('authentication:dashboard')
        else:
            # Form is not valid, fall through to re-render the form with error messages
            pass
    else:
        form = UserLoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    # Перенаправление на главную страницу после выхода
    return redirect('index')


@login_required(login_url='/authentication/login/')
def dashboard(request):
    # Проверка параметра запроса для редактирования
    edit = request.GET.get('edit', 'false') == 'true'
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваши данные успешно обновлены.")
            return redirect('authentication:dashboard')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'authentication/dashboard.html', {'form': form, 'edit': edit})


class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'authentication/password_reset_form.html'
    email_template_name = 'authentication/password_reset_email.html'
    success_url = reverse_lazy('authentication:password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('authentication:password_reset_complete')


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'authentication/dashboard.html'
    success_url = reverse_lazy('authentication:password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_change_form'] = context.get('form')
        return context
