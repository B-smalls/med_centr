from django.db import models

class ServShedule(models.Model):
    serv_day = models.DateField('serv_day')
    serv_hours = models.TimeField('serv_hours')
    serv_status = models.BooleanField('serv_status', default=False)
    serv_id = models.ForeignKey(
        'medservices.Service', models.CASCADE
    )