import pytest

from django.urls import reverse
from rest_framework import status

from ..models import Category
from ...tests.fixtures_category import CategoryFactory

@pytest.mark.django_db
def test_create_category(api_client):
    """
    Test creating a new category through the API.
    """
    url = reverse('category-list')
    data = {
        "name": "New Category",
        "categorydescription": "Description for a new category."
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Category.objects.count() == 1

@pytest.mark.django_db
def test_list_categories(api_client):
    """
    Test listing all categories through the API.
    """
    # Create some sample categories using your factory or fixtures
    categories = CategoryFactory.create_batch(5)

    url = reverse('category-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(categories)

@pytest.mark.django_db
def test_retrieve_category(api_client, category):
    """
    Test retrieving a specific category by ID through the API.
    """
    # Create a sample category using your factory or fixtures
    url = reverse('category-detail', args=[category.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == category.id

@pytest.mark.django_db
def test_update_category(api_client, category):
    """
    Test updating a specific category through the API.
    """
    # Create a sample category using your factory or fixtures

    url = reverse('category-detail', args=[category.id])
    data = {
        "name": "Updated Category",
        "categorydescription": "Updated description."
    }
    response = api_client.put(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    category.refresh_from_db()
    assert category.name == "Updated Category"

@pytest.mark.django_db
def test_delete_category(api_client, category):
    """
    Test deleting a specific category through the API.
    """
    # Create a sample category using your factory or fixtures

    url = reverse('category-detail', args=[category.id])
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Category.objects.filter(id=category.id).exists()
