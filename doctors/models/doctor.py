from django.db import models

class Doctor(models.Model):
    surname = models.CharField('surname', max_length=100)
    name = models.CharField('name', max_length=100)
    middle_name = models.CharField('middle_name', max_length=100)
    doctor_cost = models.IntegerField('doctor_cost')