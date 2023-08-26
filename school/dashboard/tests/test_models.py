import pytest
from datetime import date, timedelta

from ..enrollment_strategie import DefaultEnrollmentStrategy, PremiumEnrollmentStrategy


@pytest.mark.django_db
def test_person_creation(person_student):
    assert str(person_student) == f"{person_student.user.username} - {person_student.role}"


@pytest.mark.django_db
def test_enrollment_creation(enrollment):
    assert str(enrollment) == f"{enrollment.student.user.username} - {enrollment.course.name}"


