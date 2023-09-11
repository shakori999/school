import pytest
from django.utils import timezone
@pytest.mark.django_db
def test_student_creation(student):
    assert str(student) == f"{student.user.user.first_name} {student.user.user.last_name}"

@pytest.mark.django_db
def test_enrollment_creation(enrollment):
   assert str(enrollment) == f"{enrollment.student.full_name()} - {enrollment.course_per_cycle.course.name}"
   assert str(enrollment.enrollmentdate) == str(timezone.now().date())

