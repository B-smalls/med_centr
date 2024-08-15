from django.db import models

class Document(models.Model):
    decription = models.TextField('decription')
    dock_path = models.FileField(upload_to='document/')
    date_download = models.DateField('dock_created')
    mbook_id = models.ForeignKey(
        'medbooks.MedBook', models.CASCADE
    )
