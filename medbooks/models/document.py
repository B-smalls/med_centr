from django.db import models

from .medicalBook import MedBook

class Conclusion(models.Model):
    decription = models.TextField('decription')
    dock_path = models.TextField('dock_path')
    date_download = models.DateField('concl_created')
