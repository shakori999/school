from rest_framework import serializers

from django.utils import timezone

from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  # Include all fields from the model

    def validate(self, data):
        """
        Custom validation for the serializer data.
        """
        timearrive = data.get('timearrive')
        timeleave = data.get('timeleave')

        if timearrive > timeleave:
            raise serializers.ValidationError("Arrival time must be before leave time.")

        if timearrive  > timezone.now():
            raise serializers.ValidationError("Arrival time cannot be in the future.")

        return data

    def create(self, validated_data):
        # Automatically set the timearrive field to the current time
        validated_data['timearrive'] = timezone.now()
        return super().create(validated_data)
