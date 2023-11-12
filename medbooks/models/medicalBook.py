from django.db import models
class MedBook(models.Model):
    card_number = models.CharField('card_number', max_length=50)
    status = models.BooleanField('status', default=True)
    date_created = models.DateField('date_created')
    account_id = models.BigIntegerField('account_id')

class Meta:
    verbose_name = 'Медицинская книжка'
    verbose_name_plural = 'Медицинские книжки'
    ordering = ('card_number', )