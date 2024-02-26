from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from doctors.serializers.nested import specializations
from doctors.models.specialization import Specialization


@extend_schema_view(
    get=extend_schema(request=specializations.SpecializationSerializer,
                      summary='Получение списка всех специализаций', tags=['Врачи']),
)
class SpacializationsAllView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = specializations.SpecializationSerializer
    queryset = Specialization.objects.all()
