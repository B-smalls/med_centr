from django.db import models

class Document(models.Model):
    decription = models.TextField('decription')
    dock_path = models.TextField('dock_path')
    date_download = models.DateField('dock_created')
    mbook_id = models.ForeignKey(
        'medbooks.MedBook', models.CASCADE
    )
