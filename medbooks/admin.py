from django.contrib import admin
from medbooks.models.medicalBook import MedBook
from medbooks.models.result import Result
from medbooks.models.document import Document
from medbooks.models.conclusion import Conclusion

@admin.register(MedBook)
class MedBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_number', 'status', 'date_created', 'account_id',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'decription', 'dock_path', 'res_created', 'serv_id', 'mbook_id')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'decription', 'dock_path', 'date_download', 'mbook_id',)

@admin.register(Conclusion)
class ConclusionAdmin(admin.ModelAdmin):
    list_display = ('id', 'decription', 'dock_path', 'concl_created', 'doctor_id', 'mbook_id')
