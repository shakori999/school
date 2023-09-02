import pytest

@pytest.mark.django_db
def test_category_creation(category):
    assert str(category) == f"{category.name}"

