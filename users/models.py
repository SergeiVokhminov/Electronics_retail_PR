from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Поля для модели пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    avatar = models.ImageField(
        upload_to="photo/avatars/", verbose_name="Аватар", blank=True, null=True
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return self.email

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
