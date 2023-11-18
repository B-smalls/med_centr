from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from medservices.serializers.api import service
from medservices.models.service import Service


@extend_schema_view(
    get=extend_schema(request=service.ServiceSerializer,
                      summary='Получение списка всех услуг и их стоимости', tags=['Медицинские услуги']),
)
class ServiceAllView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = service.ServiceSerializer
