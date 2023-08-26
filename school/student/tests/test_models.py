import pytest

@pytest.mark.django_db
def test_student_creation(student):
    assert str(student) == f"{student.user.user.first_name} {student.user.user.last_name}"
