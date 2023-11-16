from django.db import models


class Result(models.Model):
    decription = models.TextField('decription')
    dock_path = models.TextField('dock_path')
    res_created = models.DateField('res_created')
    serv_id = models.IntegerField('serv_id')
    mbook_id = models.ForeignKey(
        'medbooks.MedBook', models.CASCADE
    )