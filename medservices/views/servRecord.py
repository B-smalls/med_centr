from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from medservices.models.servRecord import ServRecord
from medservices.models.servShedule import ServShedule
from medservices.serializers.api import servRecord
from medservices.serializers.api.servRecord import ServRecordSerializer


@extend_schema_view(
    post=extend_schema(
        summary='Создание записи на мед. услугу', tags=['Медицинские услуги']),
)
class ServRecordCreateView(APIView):
    def post(self, **kwargs):
        sshed_id = kwargs.get('sshed_id')
        serializer = ServRecordSerializer(context={'sshed_id': sshed_id})

        # Пытаемся валидировать данные
        if serializer.is_valid():
            # Сохраняем запись
            serializer.save()
            # Возвращаем успешный ответ с данными созданной записи
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные не прошли валидацию, возвращаем ошибку
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

