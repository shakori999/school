import pytest
from datetime import date, timedelta

@pytest.mark.django_db
def test_Role_student_creation(create_student_role):
    assert str(create_student_role) == f"student"

@pytest.mark.django_db
def test_Role_teacher_creation(create_teacher_role):
    assert str(create_teacher_role) == f"teacher"

@pytest.mark.django_db
def test_person_student_creation(person_student):
    assert str(person_student) == f"{person_student.user.username} - {person_student.role}"

@pytest.mark.django_db
def test_person_teacher_creation(person_teacher):
    assert str(person_teacher) == f"{person_teacher.user.username} - {person_teacher.role}"



