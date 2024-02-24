from django.utils import timezone

from rest_framework import serializers
from medservices.models.servShedule import ServShedule
from medservices.models.servRecord import ServRecord
from django.db import transaction
from medservices.serializers.nested import services
from rest_framework.exceptions import ParseError
from django.http import HttpResponse

class ServRecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServRecord
        fields = (
            'id',
            'servRecord_date',
            'sshed_id',
        )

    def create(self, validated_data):
        try:
            sshed_id = self.initial_data.get('sshed_id')
            account_id = self.context['request'].user.id  # Получаем id пользователя из запроса

            with transaction.atomic():
                record = ServRecord.objects.create(account_id=account_id, **validated_data)

                ServShedule.objects.filter(id=sshed_id).update(serv_status=False)
        except Exception as e:
            raise ParseError(f"Ошибка при создании записи: {e}")

        return record
class ServRecordViewSerializer(serializers.ModelSerializer):
    serv_name = serializers.CharField(source='sshed_id.serv_id.serv_name', read_only=True)
    serv_day = serializers.DateField(source='sshed_id.serv_day', read_only=True)
    serv_hours = serializers.TimeField(source='sshed_id.serv_hours', read_only=True)

    class Meta:
        model = ServRecord
        fields = (
            'id',
            'servRecord_date',
            'serv_name',
            'serv_day',
            'serv_hours',
        )


class ServRecordDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def delete_record(self):
        serv_record_id = self.validated_data.get('id')
        try:
            with transaction.atomic():
                serv_record = ServRecord.objects.select_for_update().get(id=serv_record_id)
                if serv_record.account_id != self.context['request'].user.id:
                    raise serializers.ValidationError("У вас нет прав на удаление этой записи")

                serv_record.delete()  # Удаление записи ServRecord

                # Обновление serv_status в связанной записи ServShedule
                serv_shedule = serv_record.sshed_id
                serv_shedule.serv_status = True
                serv_shedule.save()
        except ServRecord.DoesNotExist:
            raise serializers.ValidationError("Запись не найдена")