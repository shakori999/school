import pytest

@pytest.mark.django_db
def test_student_creation(student, enrollment):
    assert str(student) == f"{student.user.user.first_name} {student.user.user.last_name}"

@pytest.mark.django_db
def test_enrollment_creation(enrollment):
   assert str(enrollment) == f"{enrollment.student.full_name()} - {enrollment.course_per_cycle.course.name}"
   assert str(enrollment.enrollmentdate) == f"2023-01-01"

