from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager


class Account(AbstractUser):
    username = models.CharField(verbose_name="Логин", unique=True, null=False, max_length=50)
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(
        upload_to='user_pic',
        verbose_name='Аватар',
    )
    information = models.CharField(
        null=True,
        blank=True,
        verbose_name="Информация",
        max_length=50
    )
    phone = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Номер"
    )
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Имя"
    )
    gender = models.CharField(
        max_length=50,
        default=1,
        choices=(('Мужской', 'Мужской'), ('Женский', 'Женский'))
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Лайки',
        to='posts.Post',
        related_name='user_likes')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунт'
