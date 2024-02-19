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
class ServRecordCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servRecord.ServRecordSerializer

