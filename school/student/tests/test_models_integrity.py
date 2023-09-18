import pytest
from django.db import IntegrityError
from django.test import TestCase
from ..models import Student

@pytest.mark.django_db
def test_student_name_unique(create_student_role):
    # Create a student with a specific studentname
    Student.objects.create(
            studentname="Test Student",
            email="test@example.com",
            birthdate="2000-01-01",
            phoneno="1234567890",
        )
    # Try to create another student with the same studentname, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Student.objects.create(
                studentname="Test Student",
                email="another@example.com",
                birthdate="2001-01-01",
                phoneno="9876543210"
        )

@pytest.mark.django_db
def test_email_unique(create_student_role):
    # Create a student with a specific email
    Student.objects.create(
            studentname="First Student",
            email="test@example.com",
            birthdate="2000-01-01",
            phoneno="1234567890"
        )
    # Try to create another student with the same email, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Student.objects.create(
                studentname="Second Student",
                email="test@example.com",
                birthdate="2001-01-01",
                phoneno="9876543210"
        )

@pytest.mark.django_db
def test_phoneno_unique(create_student_role):
    # Create a student with a specific phoneno
    Student.objects.create(
            studentname="Test Student",
            email="test@example.com",
            birthdate="2000-01-01",
            phoneno="1234567890"
        )
    # Try to create another student with the same phoneno, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Student.objects.create(
                studentname="Another Student",
                email="another@example.com",
                birthdate="2001-01-01",
                phoneno="1234567890"
        )

@pytest.mark.django_db
def test_user_creation(create_student_role):
    # Create a student object
    student = Student(
        studentname="Test Student",
        email="test@example.com",
        birthdate="2000-01-01",
        phoneno="1234567890",
        password="studentpass123",
    )
    student.save()  # This should trigger the creation of corresponding Person and User instances
    assert student.user is not None  # Ensure that the user field is populated
