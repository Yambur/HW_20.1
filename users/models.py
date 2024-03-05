from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets
from main.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')

    code = ''.join([str(secrets.token_urlsafe(5))])
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name="верификация")
    verify_code = models.CharField(max_length=10, default=code, verbose_name='Код вeрификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

