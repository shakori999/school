from rest_framework import serializers

from .models import Teacher,TeachersPerCourse

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def validate_date_of_birth(self, value):
        if value is not None and (value.year < 1900 or value.year > 2023):
            raise serializers.ValidationError("Invalid date of birth")
        return value

class TeachersPerCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersPerCourse
        fields = '__all__'
