import pytest

from ..categories.models import Category

@pytest.fixture
def category():
    category = Category.objects.create(
        name="Sample Category",
        categorydescription="Sample Category Description",
    )
    return category

