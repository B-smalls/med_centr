from django.db import models

class ServRecord(models.Model):
    servRecord_date = models.DateField('servRecord_date', blank=True, null=True,)
    account_id = models.BigIntegerField('account_id', blank=True, null=True,)
    sshed_id = models.OneToOneField(
        'medservices.ServShedule', models.CASCADE
    )