from django.db import models

class DoctRecord(models.Model):
    doctRecord_date = models.DateField('doctRecord_date')
    account_id = models.BigIntegerField('account_id')
    dshed_id = models.OneToOneField(
        'doctors.DoctShedule', models.CASCADE
    )