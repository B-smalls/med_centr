from django.urls import path

from medbooks.views import conclusion, document, result, medicalBook


urlpatterns = [
    path('medbook/document/upload', document.DocumentUploadView.as_view(), name='upload_file'),
    path('medbook/document/download/<int:document_id>', document.DocumentDownloadView.as_view(), name='download_file'),

    path('medbook/document/list/<int:medbook_id>', document.DocumentListView.as_view(), name='list-document'),


    path('medbook/mbook/list/<int:user_id>', medicalBook.MedBookLookView.as_view(), name='medbook'),
]
