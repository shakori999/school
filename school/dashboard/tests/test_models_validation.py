import pytest
from django.db.utils import IntegrityError

@pytest.mark.django_db
def test_valid_person(valid_person):
    assert valid_person.user.username == "testuser"
    assert valid_person.username == "testusername"
    assert valid_person.password_hash == "testhash"
    assert valid_person.email == "test@example.com"
    assert valid_person.role.role_name == "student"

@pytest.mark.django_db
def test_invalid_person(invalid_person):
    with pytest.raises(Exception):  # Adjust the specific exception type if needed
        invalid_person.save()

@pytest.mark.django_db
def test_unique_constraint(duplicate_person):
    with pytest.raises(IntegrityError):
        duplicate_person.save()
