from django.utils import timezone

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

    def create(self):
        user = self.context['request'].user
        sshed_id = self.context.get('sshed_id')
        current_date = timezone.now().date()
        print("SSSSSSS", sshed_id)
        try:
            with transaction.atomic():
                # Создаем запись с указанием текущей даты, ID пользователя и sshed_id
                serv_record = ServRecord.objects.create(
                    servRecord_date=current_date,
                    account_id=user.id,
                    sshed_id=sshed_id,
                )

                # Обновляем 'serv_status' в модели ServShedule
                schedule_instance = ServShedule.objects.get(id=sshed_id)
                schedule_instance.serv_status = False
                schedule_instance.save()

        except ServShedule.DoesNotExist:
            raise serializers.ValidationError(f"servShedule с sshed_id {sshed_id} не найден.")
        except Exception as e:
            raise serializers.ValidationError(f"Произошла ошибка при создании записи: {str(e)}")

        return serv_record