from rest_framework import serializers

from doctors.models.specialization import Specialization


class SpecializationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Specialization
        fields = (
            'id',
            'special_name'
        )