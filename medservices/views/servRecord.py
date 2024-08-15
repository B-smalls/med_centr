from django.utils import timezone
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from medservices.models.servRecord import ServRecord
from medservices.models.servShedule import ServShedule
from medservices.serializers.api import servRecord
from medservices.serializers.api.servRecord import ServRecordCreateSerializer


@extend_schema_view(
    post=extend_schema(request=servRecord.ServRecordCreateSerializer,
                      summary='Создание записи на мед. услугу', tags=['Медицинские услуги']),
)
class ServRecordCreateView(APIView):
    def post(self, request):
        serializer = ServRecordCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Запись успешно создана"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema_view(
    delete=extend_schema(request=servRecord.ServRecordDeleteSerializer,
                         summary='Удаление записи на мед. услугу', tags=['Медицинские услуги'])
)
class ServRecordDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):  # pk будет содержать идентификатор записи из URL
        serializer = servRecord.ServRecordDeleteSerializer(data={'id': pk}, context={'request': request})
        if serializer.is_valid():
            serializer.delete_record()
            return Response({"message": "Запись успешно удалена и статус обновлен"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    get=extend_schema(request=servRecord.ServRecordViewSerializer,
                         summary='Получение активных записей на мед. услуги для пользователя', tags=['Медицинские услуги'])
)
class ServRecordListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Получаем текущего пользователя
        # Фильтруем записи по пользователю и каким-то условиям активности
        user_records = ServRecord.objects.filter(account_id=user.id)
        serializer = servRecord.ServRecordViewSerializer(user_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)