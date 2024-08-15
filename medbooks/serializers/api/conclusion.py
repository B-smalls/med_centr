from rest_framework import serializers

from medbooks.models.conclusion import Conclusion
class ConclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conclusion
        fields = ('id', 'description', 'dock_path', 'date_download', 'mbook_id')