from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from medservices.serializers.api import servShedule
from medservices.models.servShedule import ServShedule


#Получение расписания мед. услуг
@extend_schema_view(
    get=extend_schema(request=servShedule.ServSheduleSerializer,
                      summary='Получение расписания медицинских услуг', tags=['Медицинские услуги']),
)
class ServSheduleView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servShedule.ServSheduleSerializer

    def get_queryset(self):
        return ServShedule.objects.filter(serv_status=True)


#Получение расписания по id
@extend_schema_view(
    get=extend_schema(request=servShedule.SearchSheduleSerializer,
                      summary='Получение расписания медицинских услуг по id услуги', tags=['Медицинские услуги']),
)
class SearchSheduleView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servShedule.SearchSheduleSerializer

    def get_queryset(self):
        serv_id = self.kwargs.get('serv_id')

        if serv_id is not None and isinstance(serv_id, int):
            return ServShedule.objects.filter(serv_id=serv_id, serv_status=True)

        return ServShedule.objects.none()


