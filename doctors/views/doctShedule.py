from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView


from doctors.serializers.api import doctShedule
from doctors.models.doctShedule import DoctShedule


@extend_schema_view(
    get=extend_schema(request=doctShedule.DoctorSheduleSerializer,
                      summary='Получение всего расписания', tags=['Врачи']),
)
class DoctSheduleAllView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = doctShedule.DoctorSheduleSerializer
    queryset = DoctShedule.objects.all()


@extend_schema_view(
    get=extend_schema(request=doctShedule.DoctorSheduleSerializer,
                      summary='Получение расписания по врачу', tags=['Врачи']),
)
class DoctSheduleByDoctView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        doctor_id = self.kwargs.get('doctor_id')
        doctors_list = DoctShedule.objects.filter(doctor_id=doctor_id)
        serializer = doctShedule.DoctorSheduleSerializer(doctors_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@extend_schema_view(
    get=extend_schema(request=doctShedule.DoctorSheduleSerializer,
                      summary='Получение расписания по специализации', tags=['Врачи']),
)
class DoctSheduleBySpecView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        special_id = self.kwargs.get('special_id')
        doctors_list = DoctShedule.objects.filter(doctor_id__special_id=special_id)
        serializer = doctShedule.DoctorSheduleSerializer(doctors_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
