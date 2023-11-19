from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from medservices.serializers.api import servRecord


@extend_schema_view(
    post=extend_schema(request=servRecord.ServRecordSerializer,
                       summary='Создание записи на мед. услугу', tags=['Медицинские услуги']),
)
class ServRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Создаем экземпляр сериализатора с переданными данными запроса
        serializer = servRecord.ServRecordSerializer(data=request.data, context={'request': request})

        # Пытаемся валидировать и создать запись
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
