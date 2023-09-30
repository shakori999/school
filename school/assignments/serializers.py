from rest_framework import serializers

from django.utils import timezone

from .models import Assignment, Submission

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'course', 'title', 'description', 'due_date')

    def validate_due_date(self, value):
        # Ensure due_date is not in the past
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

class SubmissionSerializer(serializers.ModelSerializer):

    assignment = serializers.CharField()
    student = serializers.CharField()

    class Meta:
        model = Submission
        fields = ('id', 'assignment', 'student', 'submission_date', 'file_upload')

    def validate_submission_date(self, value):
        # Ensure submission_date is not in the future
        if value > timezone.now().date():
            raise serializers.ValidationError("Submission date cannot be in the future.")
        if value < timezone.now().date():
            raise serializers.ValidationError("Submission date cannot be in the past.")
        return value

    def validate_file_upload(self, value):
        # Add your file validation logic here
        # Example: Check file size or file type
        # Replace the following line with your own validation
        if value.size > 10 * 1024 * 1024:  # 10 MB
            raise serializers.ValidationError("File size cannot exceed 10 MB.")
        return value
