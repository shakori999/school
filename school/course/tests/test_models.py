import pytest

@pytest.mark.django_db
def test_course_creation(course):
    assert str(course) == f"Mathematics 101"
