from rest_framework import serializers
from medservices.models.servShedule import ServShedule
from medservices.models.servRecord import ServRecord
from django.db import transaction
from rest_framework.exceptions import ParseError
from django.http import HttpResponse

class ServRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServRecord
        fields = (
            'id',
            'servRecord_date',
            'account_id',
            'sshed_id',
        )

    def create(self, validated_data):
        # Получаем текущего пользователя из контекста запроса
        user = self.context['request'].user

        # Получаем 'sshed_id' из данных запроса
        sshed_id = validated_data.get('sshed_id')

        # Добавляем текущего пользователя в данные перед сохранением записи
        validated_data['account_id'] = user

        try:
            with transaction.atomic():
                # Создаем запись
                serv_record = super(ServRecordSerializer, self).create(validated_data)

                # Обновляем 'serv_status' в модели servShedule
                schedule_instance = ServShedule.objects.select_for_update().get(sshed_id=sshed_id)
                schedule_instance.serv_status = True
                schedule_instance.save()

        except ServShedule.DoesNotExist:
            raise ParseError(f"servShedule с sshed_id {sshed_id} не найден.")
        except Exception as e:
            raise ParseError(f"Произошла ошибка при создании записи: {str(e)}")

        return serv_record
