from rest_framework import serializers
from .models import Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_classno(self, value):
        if value < 0:
            raise serializers.ValidationError("Class number must be greater than or equal to 0")
        return value

    def create(self, validated_data):
        # Customize create logic here if needed
        return Class.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Customize update logic here if needed
        instance.classtitle = validated_data.get('classtitle', instance.classtitle)
        instance.save()
        return instance
