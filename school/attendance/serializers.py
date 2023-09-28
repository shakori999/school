from rest_framework import serializers

from django.utils import timezone
from rest_framework.fields import TimeField

from .models import Attendance

class CustomTimeField(serializers.Field):
    def to_representation(self, value):
        # Convert the Python datetime.time object to a string
        return value.strftime('%H:%M:%S')

    def to_internal_value(self, data):
        # Parse the input string and return a datetime.time object
        from datetime import time
        try:
            return time.fromisoformat(data)
        except ValueError:
            raise serializers.ValidationError("Invalid time format. Use ISO 8601 format (HH:MM:SS).")

class AttendanceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Attendance
        fields = ['course','cycle', 'student','class_info','timearrive','timeleave']


    def create(self, validated_data):

        # Automatically set the timearrive field to the current time
        validated_data['timearrive'] = timezone.now().time()

        class_info = validated_data.get('class_info')
        print(class_info.endtime)


        # Automatically set the timeleave field based on class_date and class_endtime
        validated_data['timeleave'] = class_info.endtime
        

        # Create a new instance of the Attendance model with the updated data
        attendance = Attendance(**validated_data)
        attendance.save()

        return attendance

    def validate(self, data):
        """
        Custom validation for the serializer data.
        """
        timearrive = data.get('timearrive')
        timeleave = data.get('timeleave')
        if timearrive is None or timeleave is None:
            raise serializers.ValidationError("Both arrival and leave times must be provided.")

        if timearrive >= timeleave:
            raise serializers.ValidationError("Arrival time must be before leave time.")

        return data
