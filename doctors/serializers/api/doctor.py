from rest_framework import serializers
from doctors.models.doctor import Doctor
from doctors.serializers.nested.specializations import SpecializationSerializer

class DoctorSerializer(serializers.ModelSerializer):

    special_id = SpecializationSerializer()
    class Meta:
        model = Doctor
        fields = (
            'id',
            'surname',
            'name',
            'middle_name',
            'doctor_cost',
            'special_id'
        )

