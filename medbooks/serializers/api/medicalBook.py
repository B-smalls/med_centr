from rest_framework import serializers
from django.utils import timezone
from medbooks.models.medicalBook import MedBook
class MBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedBook
        fields = (
            'id',
            'card_number',
            'status',
            'date_created',
            'account_id'
        )