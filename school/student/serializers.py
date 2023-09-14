from rest_framework import serializers
from django.utils import timezone

from .models import Student, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',"user")

    def validate_phoneno(self, value):
        # Custom validation logic for the 'phoneno' field
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value

    def validate_email(self, value):
        # Custom validation logic for the 'email' field
        if not value.endswith('.com'):
            raise serializers.ValidationError("Email must be in the 'example.com' domain.")
        return value

    def validate_birthdate(self, value):
        # Custom validation logic for the 'birthdate' field
        if value > timezone.now().date():
            raise serializers.ValidationError("Birthdate cannot be in the future.")
        return value

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_enrollmentdate(self, value):
        # Custom validation for the 'enrollmentdate' field
        if value and value > timezone.now().date():
            raise serializers.ValidationError("Enrollment date cannot be in the future.")
        return value

    def validate_cancellationreason(self, value):
        # Custom validation for the 'cancellationreason' field
        if self.initial_data.get('cancelled') and not value:
            raise serializers.ValidationError("Cancellation reason is required for canceled enrollments.")
        return value
