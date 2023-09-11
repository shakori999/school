import pytest
from datetime import date

from django.core.exceptions import ValidationError

from ..models import Student, Enrollment

'''
this section for testing Student model
'''

@pytest.mark.django_db
def test_required_fields_are_provided(student):
    with pytest.raises(ValidationError):
        student.full_clean()

@pytest.mark.django_db
def test_valid_email():
    with pytest.raises(ValidationError):
        student = Student(email="invalid_email")
        student.full_clean()

@pytest.mark.django_db
def test_birthdate_in_past():
    with pytest.raises(ValidationError):
        student = Student(birthdate="2050-01-01")
        student.full_clean()

@pytest.mark.django_db
def test_valid_phone_number_format():
    with pytest.raises(ValidationError):
        student = Student(phoneno="12345")  # Invalid phone number format
        student.full_clean()

@pytest.mark.django_db
def test_address_max_length():
    with pytest.raises(ValidationError):
        student = Student(address="A" * 1000)  # Exceeds max length
        student.full_clean()

'''
this section for testing Enrollment model
'''

@pytest.mark.django_db
def test_required_fields_are_provided(enrollment):
    # Test creating an Enrollment with required fields
    enrollment.full_clean()  # Should not raise a ValidationError

@pytest.mark.django_db
def test_enrollmentdate_in_past(course_per_cycle, student):
    # Test creating an Enrollment with enrollment date in the past
    with pytest.raises(ValidationError, match="Enrollment date cannot be in the past"):
        enrollment = Enrollment(
            course_per_cycle=course_per_cycle,
            student=student,
            enrollmentdate=date(2000, 1, 1),  # Date in the past
        )
        enrollment.full_clean()

@pytest.mark.django_db
def test_cancellation_with_reason(course_per_cycle, student):
    # Test creating a canceled Enrollment with a cancellation reason
    enrollment = Enrollment(
        course_per_cycle=course_per_cycle,
        student=student,
        enrollmentdate=date(2023, 9, 15),
        cancelled=True,
        cancellationreason="Not interested anymore",
    )
    enrollment.full_clean()  # Should not raise a ValidationError

@pytest.mark.django_db
def test_cancellation_without_reason(course_per_cycle, student):
    # Test creating a canceled Enrollment without a cancellation reason
    with pytest.raises(ValidationError, match="Cancellation reason is required for canceled enrollments"):
        enrollment = Enrollment(
            course_per_cycle=course_per_cycle,
            student=student,
            enrollmentdate=date(2023, 9, 15),
            cancelled=True,
        )
        enrollment.full_clean()

