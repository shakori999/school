import pytest

@pytest.mark.django_db
def test_teacher_creation(teacher):
    assert str(teacher) == f"{teacher.user.user.first_name} {teacher.user.user.last_name}"
