from rest_framework import serializers
from medservices.models.service import Service


class ServiceShotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'id',
            'serv_name',
        )