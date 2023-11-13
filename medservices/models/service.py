from django.db import models

class Service(models.Model):
    serv_name = models.TextField('serv_name')
    serv_cost = models.IntegerField('serv_cost')