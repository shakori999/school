from rest_framework import serializers

from django.utils import timezone

from .models import Test, TestsScores

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def validate_testdate(self, value):
        """
        Custom validation to ensure that the test date is not in the past.
        """
        if value < timezone.now().date():
            raise serializers.ValidationError("Test date cannot be in the past")
        return value

class TestScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestsScores
        fields = '__all__'

    def validate_score(self, value):
        """
        Custom validation to ensure that the score is between 0 and 100.
        """
        if value < 0 or value > 100:
            raise serializers.ValidationError("Score must be between 0 and 100")
        return value

    def validate_testsno(self, value):
        """
        Custom validation to ensure that testsno is greater than or equal to 1.
        """
        if value is not None and value <= 0:
            raise serializers.ValidationError("Ensure this value is greater than or equal to 1")
        return value
