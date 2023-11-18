from rest_framework import serializers
from medservices.models.servShedule import ServShedule
from medservices.serializers.nested import services


class ServSheduleSerializer(serializers.ModelSerializer):

    serv_id = services.ServiceShotSerializer()
    class Meta:
        model = ServShedule
        fields = (
            'id',
            'serv_day',
            'serv_hours',
            'serv_status',
            'serv_id',
        )


class SearchSheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServShedule
        fields = (
            'id',
            'serv_day',
            'serv_hours',
            'serv_id'
        )