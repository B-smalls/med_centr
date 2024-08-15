from doctors.models.doctRecord import DoctRecord
from doctors.models.doctShedule import DoctShedule

from rest_framework import serializers
from django.db import transaction
from rest_framework.exceptions import ParseError
from django.http import HttpResponse

class DoctRecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctRecord
        fields = (
            'id',
            'doctRecord_date',
            'dshed_id',
        )

    def create(self, validated_data):
        try:
            dshed_id = self.initial_data.get('dshed_id')
            account_id = self.context['request'].user.id  # Получаем id пользователя из запроса

            with transaction.atomic():
                record = DoctRecord.objects.create(account_id=account_id, **validated_data)

                DoctShedule.objects.filter(id=dshed_id).update(doct_status=False)
        except Exception as e:
            raise ParseError(f"Ошибка при создании записи: {e}")

        return record
class DoctRecordViewSerializer(serializers.ModelSerializer):
    specialization = serializers.CharField(source='dshed_id.doctor_id.special_id.special_name', read_only=True)
    surname = serializers.CharField(source='dshed_id.doctor_id.surname', read_only=True)
    name = serializers.CharField(source='dshed_id.doctor_id.name', read_only=True)
    middle_name = serializers.CharField(source='dshed_id.doctor_id.middle_name', read_only=True)
    doct_day = serializers.DateField(source='dshed_id.doc_day', read_only=True)
    doct_hours = serializers.TimeField(source='dshed_id.doct_hours', read_only=True)
    class Meta:
        model = DoctRecord
        fields = (
            'id',
            'doctRecord_date',
            'specialization',
            'surname',
            'name',
            'middle_name',
            'doct_day',
            'doct_hours',
        )


class DoctRecordDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def delete_record(self):
        doct_record_id = self.validated_data.get('id')
        try:
            with transaction.atomic():
                doct_record = DoctRecord.objects.select_for_update().get(id=doct_record_id)
                if doct_record.account_id != self.context['request'].user.id:
                    raise serializers.ValidationError("У вас нет прав на удаление этой записи")

                doct_record.delete()  # Удаление записи ServRecord

                # Обновление serv_status в связанной записи ServShedule
                doct_shedule = doct_record.dshed_id
                doct_shedule.doct_status = True
                doct_shedule.save()
        except DoctRecord.DoesNotExist:
            raise serializers.ValidationError("Запись не найдена")