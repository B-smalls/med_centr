from django.contrib import admin
from medbooks.models.medicalBook import MedBook

@admin.register(MedBook)
class MedBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_number', 'status', 'date_created', 'account_id',)
