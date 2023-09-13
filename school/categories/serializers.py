from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'categorydescription')  # Explicitly specify the fields

    def to_representation(self, instance):
        """
        Customize the representation of the serialized data.
        """
        representation = super().to_representation(instance)
        representation['description_summary'] = instance.get_description_summary()
        return representation

