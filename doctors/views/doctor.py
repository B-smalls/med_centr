from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView


from doctors.serializers.api import doctor
from doctors.models.doctor import Doctor


@extend_schema_view(
    get=extend_schema(request=doctor.DoctorSerializer,
                      summary='Получение списка всех врачей', tags=['Врачи']),
)
class DoctorsAllView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = doctor.DoctorSerializer
    queryset = Doctor.objects.all()


@extend_schema_view(
    get=extend_schema(request=doctor.DoctorSerializer,
                      summary='Получение списка всех врачей для определенной специализации', tags=['Врачи']),
)
class SearchDoctorsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        special_id = self.kwargs.get('special_id')
        doctors_list = Doctor.objects.filter(special_id=special_id)
        serializer = doctor.DoctorSerializer(doctors_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
