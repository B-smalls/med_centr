from django.db import models

from .medicalBook import MedBook

class Conclusion(models.Model):
    decription = models.TextField('decription')
    dock_path = models.TextField('dock_path')
    concl_created = models.DateField('concl_created')
    doctor_id = models.IntegerField('doctor_id')



