from django.db import models

class ServRecord(models.Model):
    servRecord = models.DateField('servRecord')
    account_id = models.BigIntegerField('account_id')
    sshed_id = models.OneToOneField(
        'medservices.ServShedule', models.CASCADE
    )