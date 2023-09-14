from django.utils import timezone
from rest_framework import serializers

from .models import Teacher,TeachersPerCourse

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',"user")

    def validate_date_of_birth(self, value):
        if value is not None and (value.year < 1900 or value.year > 2023):
            raise serializers.ValidationError("Invalid date of birth")
        return value

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

class TeachersPerCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersPerCourse
        fields = '__all__'
