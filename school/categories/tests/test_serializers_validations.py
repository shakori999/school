import pytest
from django.core.exceptions import ValidationError
from ..models import Category
from ..serializers import CategorySerializer

@pytest.mark.django_db
def test_valid_category_serializer():
    """
    Test a valid category serializer.
    """
    data = {
        "name": "Valid Category",
        "categorydescription": "This is a valid category description."
    }
    serializer = CategorySerializer(data=data)

    assert serializer.is_valid()
    assert serializer.save() is not None

@pytest.mark.django_db
def test_blank_name_serializer():
    """
    Test creating a category serializer with a blank name.
    """
    data = {
        "name": "",  # Blank name
        "categorydescription": "Description for a category with a blank name."
    }
    serializer = CategorySerializer(data=data)

    assert not serializer.is_valid()
    assert 'name' in serializer.errors

@pytest.mark.django_db
def test_long_description_serializer():
    """
    Test creating a category serializer with a description that exceeds the maximum length.
    """
    data = {
        "name": "Long Description",
        "categorydescription": "A" * 201  # Exceeds the maximum length of 100 characters
    }
    serializer = CategorySerializer(data=data)

    assert not serializer.is_valid()
    assert 'categorydescription' in serializer.errors

@pytest.mark.django_db
def test_summary_serializer():
    """
    Test the get_description_summary method of the serializer.
    """
    data = {
        "name": "Summary Test",
        "categorydescription": "This is a long description for testing the summary function."
    }
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid()
    instance = serializer.save()

    summary = instance.get_description_summary()
    assert isinstance(summary, str)
    assert summary.startswith("This is a long description")

@pytest.mark.django_db
def test_short_summary_serializer():
    """
    Test the get_description_summary method with a short description.
    """
    data = {
        "name": "Short Summary Test",
        "categorydescription": "Short description."
    }
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid()
    instance = serializer.save()

    summary = instance.get_description_summary()
    assert isinstance(summary, str)
    assert summary == "Short description."

@pytest.mark.django_db
def test_unicode_representation_serializer():
    """
    Test the string representation of the serializer.
    """
    data = {
        "name": "Unicode Category",
        "categorydescription": "Description for a category with Unicode characters: ŞĞİıČĐř"
    }
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid()
    instance = serializer.save()

    assert str(instance) == "Unicode Category"
