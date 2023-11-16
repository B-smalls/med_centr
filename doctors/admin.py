from django.contrib import admin
from doctors.models.doctor import Doctor
from doctors.models.doctRecord import DoctRecord
from doctors.models.doctShedule import DoctShedule
from doctors.models.specialization import Specialization

# Register your models here.

@admin.register(Specialization)
class ServRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'special_name')

@admin.register(Doctor)
class ServRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'middle_name', 'doctor_cost', 'special_id')

@admin.register(DoctRecord)
class ServRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctRecord_date', 'account_id', 'dshed_id')

@admin.register(DoctShedule)
class ServRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_day', 'doct_hours', 'doct_status', 'doctor_id')


