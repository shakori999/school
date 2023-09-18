import pytest
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from ..models import Teacher



@pytest.mark.django_db
def test_unique_email(create_teacher_role):
    # Create a teacher with a specific email
    Teacher.objects.create(
        teachername="First Teacher",
        email="test@example.com",
        password="teacherpass123",
        phoneno="1234567890",
        subject_taught="Test Subject",
        date_of_birth="1990-01-01",
        address="Test Address",
    )
    # Try to create another teacher with the same email, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Teacher.objects.create(
            teachername="Second Teacher",
            email="test@example.com",
            password="teacherpass123",
            phoneno="9876543210",
            subject_taught="Test Subject",
            date_of_birth="1995-01-01",
            address="Test Address",
        )

@pytest.mark.django_db
def test_phoneno_unique(create_teacher_role):
    # Create a student with a specific phoneno
    Teacher.objects.create(
            teachername="Test Student",
            password="teacherpass123",
            subject_taught="Test Subject",
            date_of_birth="1995-01-01",
            address="Test Address",
            email="test@example.com",
            phoneno="1234567890"
        )
    # Try to create another student with the same phoneno, which should raise IntegrityError
    with pytest.raises(IntegrityError):
        Teacher.objects.create(
            teachername="Another Test Student",
            password="teacherpass123",
            subject_taught="Test Subject",
            date_of_birth="1995-01-01",
            address="Test Address",
            email="test1@example.com",
            phoneno="1234567890"
        )
