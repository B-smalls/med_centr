from django.db import models

class Doctor(models.Model):
    surname = models.CharField('surname', max_length=100)
    name = models.CharField('name', max_length=100)
    middle_name = models.CharField('middle_name', max_length=100)
    doctor_cost = models.DecimalField('doctor_cost', max_digits=7, decimal_places=2)
    special_id  = models.ForeignKey(
        'doctors.Specialization', models.RESTRICT
    )