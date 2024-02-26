from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from doctors.serializers.api.doctRecord import DoctRecordCreateSerializer, DoctRecordViewSerializer, DoctRecordDeleteSerializer
from doctors.models.doctRecord import DoctRecord

@extend_schema_view(
    post=extend_schema(request=DoctRecordCreateSerializer,
                      summary='Создание записи к врачу', tags=['Врачи']),
)
class DoctRecordCreateView(APIView):
    def post(self, request):
        serializer = DoctRecordCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Запись успешно создана"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema_view(
    delete=extend_schema(request=DoctRecordDeleteSerializer,
                         summary='Удаление записи к врачу', tags=['Врачи'])
)
class DoctRecordDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):  # pk будет содержать идентификатор записи из URL
        serializer = DoctRecordDeleteSerializer(data={'id': pk}, context={'request': request})
        if serializer.is_valid():
            serializer.delete_record()
            return Response({"message": "Запись успешно удалена и статус обновлен"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    get=extend_schema(request=DoctRecordViewSerializer,
                         summary='Получение активных записей к врачам для пользователя', tags=['Врачи'])
)
class DoctRecordListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Получаем текущего пользователя
        # Фильтруем записи по пользователю и каким-то условиям активности
        user_records = DoctRecord.objects.filter(account_id=user.id)
        serializer = DoctRecordViewSerializer(user_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)