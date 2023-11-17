from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Client(AbstractUser):
    middle_name = models.CharField('middle_name', max_length=100, blank=True)
    sex = models.CharField('sex', max_length=3)
    birthday = models.DateField('birthday', null=True, default=None)
    snils = models.CharField('snils', max_length=14)
    oms = models.CharField('oms', max_length=16)
    passport_data = models.CharField('passport_data', max_length=10)
    phone_number = PhoneNumberField('phone_number', unique=True, null=True)
    email = models.EmailField('email', unique=True, null=True)
    username = models.CharField(
        'Никнейм', max_length=64, unique=True, null=True, blank=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}{self.middle_name}'

    def __str__(self):
        return f'{self.full_name} ({self.pk})'


