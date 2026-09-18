from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.accounts.manager import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='Email Address')


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def __str__(self):
        return self.username