import pytest
import factory

from ..categories.models import Category

@pytest.fixture
def category():
    category = Category.objects.create(
        name="Sample Category",
        categorydescription="Sample Category Description",
    )
    return category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    categorydescription = factory.Faker('text')
