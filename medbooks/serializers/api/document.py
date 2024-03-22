from rest_framework import serializers
from django.utils import timezone
from medbooks.models.document import Document
class DocumentSerializer(serializers.ModelSerializer):

    decription = serializers.CharField()
    date_download = serializers.DateField(read_only=True)
    class Meta:
        model = Document
        fields = (
            'id',
            'decription',
            'dock_path',
            'date_download',
            'mbook_id'
        )

    def create(self, validated_data):
        validated_data['date_download'] = timezone.now().date()  # Устанавливаем текущую дату при создании
        return super().create(validated_data)


class DocumentDownloadSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Document
        fields = (
            'id',
            'decription',
            'dock_content',
        )


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'decription',
        )


