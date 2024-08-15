from rest_framework import serializers

from doctors.models.doctShedule import DoctShedule
from doctors.serializers.api.doctor import DoctorSerializer

class DoctorSheduleSerializer(serializers.ModelSerializer):

    doctor_id = DoctorSerializer()
    class Meta:
        model = DoctShedule
        fields = (
            'id',
            'doc_day',
            'doct_hours',
            'doct_status',
            'doctor_id'
        )
