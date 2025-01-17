from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите свою почту"
    )
    phone = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name="Телефон",
        help_text="Укажите свой номер телефона",
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Город",
        help_text="Укажите свой город",
    )
    avatar = models.ImageField(
        upload_to="users",
        null=True,
        blank=True,
        verbose_name="Аватар",
        help_text="Загрузите свой аватар",
    )
    telegram_id = models.CharField(
        max_length=255,
        verbose_name="ИД телеграм",
        help_text="Укажите ваш телеграм ИД",
        null=True,
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
