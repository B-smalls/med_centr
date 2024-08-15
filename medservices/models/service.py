from django.db import models

class Service(models.Model):
    serv_name = models.TextField('serv_name')
    serv_cost = models.DecimalField('serv_cost', max_digits=7, decimal_places=2)