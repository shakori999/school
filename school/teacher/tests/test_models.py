import pytest
from django.core.exceptions import ObjectDoesNotExist
from ..models import TeachersPerCourse

@pytest.mark.django_db
def test_teacher_creation(teacher):
    assert str(teacher) == f"{teacher.user.user.first_name} {teacher.user.user.last_name}"

"""
this section for testing teacherpercourse model
"""
@pytest.mark.django_db
def test_teachers_per_course_creation(teachers_per_course):
    assert str(teachers_per_course) == f"{teachers_per_course.teacher.full_name()} - {teachers_per_course.coursespercycle.course.name} ({teachers_per_course.cycle.cycledescription})"

@pytest.mark.django_db
def test_non_existing_teacher_per_course():
    with pytest.raises(ObjectDoesNotExist):
        TeachersPerCourse.objects.get(id=9999)  # Assuming 9999 is not a valid ID
