from django.db import models

class DoctShedule(models.Model):
    doc_day = models.DateField('doc_day')
    doct_hours = models.TimeField('doct_hours')
    doct_status = models.BooleanField('doct_status', default=False)
    doctor_id = models.ForeignKey(
        'doctors.Doctor', models.CASCADE
    )
