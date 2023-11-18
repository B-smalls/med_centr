from rest_framework import serializers
from medservices.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'id',
            'serv_name',
            'serv_cost',
        )

