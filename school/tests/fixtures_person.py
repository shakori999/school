import pytest
from django.contrib.auth.models import User

from ..dashboard.models import Person, Role


@pytest.fixture()
def create_student_role():
    role, created = Role.objects.get_or_create(role_name='student')
    return role
    #yield role
    #role.delete()

@pytest.fixture
def valid_person(create_student_role, user_student):
    """
    return a valid person instance
    """
    person = Person.objects.create(
        user=user_student,
        username="testusername",
        password_hash="testhash",
        email="test@example.com",
        role=create_student_role,
    )
    return person
    
    #yield person
    #person.delete()

@pytest.fixture
def invalid_person():
    """
    return an invalid person instance
    """
    user = User.objects.create(username="invaliduser", password="invalidpassword")
    person =  Person(
        user=user,
        username="invalid_username",  # Invalid format for username
        password_hash="invalidhash",
        email="invalid-email-format",  # Invalid email format
        role=None,  # Should fail due to foreign key constraint
    )
    return person
    
    #yield person
    #person.delete()

@pytest.fixture
def duplicate_person(valid_person):
    person =  Person(
        user=valid_person.user,
        username='valid_username',
        password_hash='hashed_password',
        email='duplicate@example.com',
        role=valid_person.role
    )
    return person

    #yield person
    #person.delete()

@pytest.fixture
def valid_persons(create_student_role):
    counter = 1  # Start the counter at 1
    def create_person(username_prefix='testuser'):
        nonlocal counter
        username = f"{username_prefix}_{counter}"
        email = f"{username}@example.com"
        role=create_student_role
        person = Person.objects.create(username=username, email=email, role=role)
        counter += 1
        return person
        #yield person
        #person.delete()
    return create_person

