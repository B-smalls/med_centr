from django.contrib import admin
from medservices.models.servRecord import ServRecord
from medservices.models.servShedule import ServShedule
from medservices.models.service import Service

@admin.register(ServRecord)
class ServRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'servRecord_date', 'account_id', 'sshed_id')


@admin.register(ServShedule)
class ServSheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'serv_day', 'serv_hours', 'serv_status', 'serv_id')

@admin.register(Service)
class ServSheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'serv_name', 'serv_cost')





