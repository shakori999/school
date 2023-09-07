import pytest

from django.db.utils import IntegrityError,DataError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from ..models import Role,Person

'''
this section for testing Role model
'''

@pytest.mark.django_db
def test_role_name_max_length():
    # Test invalid data: Role name exceeding max length
    max_length = 50
    role_name = "A" * (max_length + 1)
    
    with pytest.raises(ValidationError) as e:
        role = Role.objects.create(role_name=role_name)
        role.full_clean()
    
    assert "Ensure this value has at most 50 characters" in str(e.value)

'''
this section for testing Basemodel model

'''

@pytest.mark.django_db
def test_person_is_deleted_default(person_student):
    # Create a new object of the Person model
    person_instance = person_student
    
    # Ensure that is_deleted is set to False by default
    assert person_instance.is_deleted is False

'''
this section for testing Person model
'''

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


@pytest.mark.django_db
def test_person_user_null():
    # Test that a Person instance can be created with a null user field
    person_instance = Person(username="user1", password_hash="password", email="user@example.com", role=Role.objects.create(role_name="Role1"), user=None)
    person_instance.save()
    assert person_instance.user is None

@pytest.mark.django_db
def test_person_username_uniqueness():
    # Test that you cannot create two persons with the same username
    username = "user1"
    person1 = Person(username=username, password_hash="password1", email="user1@example.com", role=Role.objects.create(role_name="Role1"))
    person1.save()

    with pytest.raises(IntegrityError):
        person2 = Person(username=username, password_hash="password2", email="user2@example.com", role=Role.objects.create(role_name="Role2"))
        person2.save()

@pytest.mark.django_db
def test_person_password_hash_length(create_student_role,user_student):
    # Ensure that the password_hash field does not exceed a reasonable length
    password_hash = "A" * 101
    with pytest.raises(ValidationError):
        person = Person.objects.create(
                user=user_student,
                username="user",
                password_hash=password_hash,
                email="user@example.com",
                role=create_student_role
        )
        person.full_clean()

@pytest.mark.django_db
def test_person_email_validity(create_student_role, user_student):
    # Test that you cannot create a Person instance with an invalid email address
    invalid_email = "invalid-email"
    with pytest.raises(ValidationError):
        person = Person(user_student,username="user",password_hash="password",email=invalid_email, role=create_student_role)
        person.full_clean()


@pytest.mark.django_db
def test_person_role_assignment_validation_error(user_student):
    # Test that you cannot create a Person instance with a non-existing role (ValidationError)
    with pytest.raises(ValidationError) as e:
        person = Person(user=user_student, username="user", password_hash="password", email="user@example.com", role_id=999)  # Non-existing role ID
        person.full_clean()

    # Ensure that the validation error message is as expected
    assert "role instance with id 999 does not exist." in str(e.value)

"""
@pytest.mark.django_db
def test_person_user_deletion_cascades(valid_person):
    # Ensure that when a Person instance is deleted, it also deletes the associated User instance
    person = valid_person
    person.save()
    assert User.objects.filter(username="testuser").exists()
    print(person.user)

    person.delete()

    assert not Person.objects.filter(username="testuser").exists()
    assert not User.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_role_deletion_protection():
    # Ensure that you cannot delete a Role instance if it is associated with any Person
    role = Role.objects.create(role_name="Role")
    person = Person(username="user", password_hash="password", email="user@example.com", role=role)
    person.save()

    with pytest.raises(IntegrityError):
        role.delete()
"""
