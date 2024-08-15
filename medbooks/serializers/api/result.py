from rest_framework import serializers

from medbooks.models.result import Result
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'description', 'dock_path', 'date_download', 'mbook_id')