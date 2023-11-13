from django.db import models

from .medicalBook import MedBook

class Result(models.Model):
    decription = models.TextField('decription')
    dock_path = models.TextField('dock_path')
    res_created = models.DateField('concl_created')
    serv_id = models.IntegerField('doctor_id')