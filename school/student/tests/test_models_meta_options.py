import pytest

from django.db.models import Index 
from django.db import connection

from ..models import Student

@pytest.mark.django_db
def test_model_verbose_name_plural():
    """
    Test that the verbose_name_plural attribute in the model's Meta class
    is correctly set to "Students".
    """
    assert Student._meta.verbose_name_plural == "Students"

@pytest.mark.django_db
def test_model_ordering():
    """
    Test that the ordering attribute in the model's Meta class
    is correctly set to ['phoneno'].
    """
    assert Student._meta.ordering == ['phoneno']

'''
@pytest.mark.django_db
def test_student_model_indexes(create_student_role):
    # Create a Student instance for testing
    student = Student.objects.create(
        studentname="Test Student",
        email="test@example.com",
        birthdate="2000-01-01",
        phoneno="1234567890",
        address="Test Address",
    )

    # Get the list of indexes applied to the Student model's database table
    indexes = connection.introspection.get_indexes(connection, Student._meta.db_table)

    # Define the expected index name based on your model's Meta
    expected_index_name = f"{Student._meta.db_table}_phoneno_idx"

    # Check if the expected index is in the list of indexes
    assert any(index.name == expected_index_name for index in indexes)

    # Get the index object by name
    index = next(index for index in indexes if index.name == expected_index_name)

    # Check that the index is an instance of the Index class
    assert isinstance(index, Index)

    # Check that the index contains the 'phoneno' field
    assert 'phoneno' in index.fields

    # Clean up: delete the test Student instance
    student.delete()
'''
