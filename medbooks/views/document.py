from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound, HttpResponse
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from medbooks.serializers.api import document
from medbooks.models.document import Document

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import os

@extend_schema_view(
    post=extend_schema(request=document.DocumentSerializer,
                      summary='Загрузка документа на сервер', tags=['Медицинская книжка']),
)
class DocumentUploadView(generics.CreateAPIView):

    queryset = Document.objects.all()
    serializer_class = document.DocumentSerializer
    parser_classes = [MultiPartParser, FormParser]


@extend_schema_view(
    get=extend_schema(request=document.DocumentDownloadSerializer,
                      summary='Загрузка документа на клиента', tags=['Медицинская книжка']),
)
class DocumentDownloadView(APIView):
    def get(self, request, document_id):
        try:
            document = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            return Response(status=404)

        # Открываем файл и передаем его как HTTP-ответ
        with open(document.dock_path.path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{document.dock_path.name}"'
            return response

@extend_schema_view(
    get=extend_schema(request=document.DocumentListSerializer,
                      summary='Получение списка всех документов', tags=['Медицинская книжка']),
)
class DocumentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        medbook_id = self.kwargs.get('medbook_id')
        document_list = Document.objects.filter(mbook_id_id=medbook_id)
        serializer = document.DocumentListSerializer(document_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
