import pytest

@pytest.mark.django_db
def test_teacher_creation(teacher):
    assert str(teacher) == f"{teacher.user.user.first_name} {teacher.user.user.last_name}"

@pytest.mark.django_db
def test_teachers_per_course_creation(teachers_per_course):
    assert str(teachers_per_course) == f"{teachers_per_course.teacher.full_name()} - {teachers_per_course.coursespercycle.course.name} ({teachers_per_course.cycle.cycledescription})"

