from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from clients.managers import CustomUserManager


class Client(AbstractUser):
    username = models.CharField(
        'username', max_length=64, unique=True, null=True, blank=True
    )
    email = models.EmailField('email', unique=True, null=True, blank=True)
    phone_number = PhoneNumberField('phone_number', unique=True, null=True, blank=True)

    middle_name = models.CharField('middle_name', max_length=100, blank=True, null=True,)
    sex = models.CharField('sex', max_length=3, blank=True, null=True,)
    birthday = models.DateField('birthday', blank=True, null=True,)
    snils = models.CharField('snils', max_length=14, blank=True, null=True,)
    oms = models.CharField('oms', max_length=16, blank=True, null=True,)
    passport_data = models.CharField('passport_data', max_length=10, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}{self.middle_name}'

    def __str__(self):
        return f'{self.full_name} ({self.pk})'


