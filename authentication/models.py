# authentication/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email address is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=150, default='', verbose_name='Фамилия')
    first_name = models.CharField(max_length=150, default='', verbose_name='Имя')
    middle_name = models.CharField(max_length=150, default='', verbose_name='Отчество', blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Мужской', 'Мужской'), ('Женский', 'Женский')), verbose_name="Пол", null=True, blank=True)
    citizenship = models.CharField(max_length=150, verbose_name='Гражданство', blank=True)
    residence = models.CharField(max_length=255, verbose_name='Место жительства', blank=True)
    medical_data = models.TextField(verbose_name="Медицинские данные", blank=True)
    diagnostic_history = models.TextField(verbose_name="История диагностик", blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=False)  # По умолчанию пользователь не активирован
    activation_date = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
