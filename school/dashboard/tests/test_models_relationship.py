import pytest

@pytest.mark.django_db
def test_person_has_role(person_student):
    assert person_student.role != "" or None

@pytest.mark.django_db
def test_person_user_relationship(person_student):
    assert person_student.user != None

@pytest.mark.django_db
def test_person_string_representation(person_student):
    expected_str = f"{person_student.user.username} - {person_student.role}"
    assert str(person_student) == expected_str
