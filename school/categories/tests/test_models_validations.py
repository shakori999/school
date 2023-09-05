import pytest

from django.core.exceptions import ValidationError

from ..models import Category

@pytest.mark.django_db
def test_valid_category():
    # Test valid data
    category = Category(name="Valid Category", categorydescription="A valid category description.")
    category.full_clean()  # This should not raise a ValidationError

@pytest.mark.django_db
def test_blank_name():
    # Test blank name field
    with pytest.raises(ValidationError) as e:
        category = Category(name="", categorydescription="A description.")
        category.full_clean()
    assert "name" in e.value.error_dict

@pytest.mark.django_db
def test_name_max_length():
    # Test name exceeding max length
    max_length = 100
    name = "A" * (max_length + 1)
    with pytest.raises(ValidationError) as e:
        category = Category(name=name, categorydescription="A description.")
        category.full_clean()
    assert "Ensure this value has at most 100 characters" in str(e.value)

@pytest.mark.django_db
def test_blank_categorydescription():
    # Test blank categorydescription field
    with pytest.raises(ValidationError) as e:
        category = Category(name="Valid Category", categorydescription="")
        category.full_clean()
    assert "categorydescription" in e.value.error_dict
