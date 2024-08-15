from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound, HttpResponse
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from medbooks.models.medicalBook import MedBook
from medbooks.serializers.api import medicalBook
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import os
@extend_schema_view(
    get=extend_schema(request=medicalBook.MBookSerializer,
                      summary='Получение медкарты по id пользователя', tags=['Медицинская книжка']),
)
class MedBookLookView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        document_list = MedBook.objects.filter(account_id=user_id)
        if not document_list.exists():
            return JsonResponse({"error": "Такого аккаунта нет"}, status=status.HTTP_404_NOT_FOUND)

        serializer = medicalBook.MBookSerializer(document_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)