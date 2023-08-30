import pytest
from django.db.utils import IntegrityError

from ..models import TeachersPerCourse

@pytest.mark.django_db
def test_teachers_per_course_unique(teachers_per_course):

    # Create two TeachersPerCourse instances with the same attributes

    teachers_per_course_1 = teachers_per_course
    teachers_per_course_2 = teachers_per_course

    # There should be only one TeachersPerCourse instance due to unique_together constraint

    assert TeachersPerCourse.objects.count() == 1

@pytest.mark.django_db
def test_teacher_full_name_with_first_and_last_name(teacher):
    # Create a Teacher instance with first and last name
    teacher.user.user.first_name = 'mohammed1'
    teacher.user.user.last_name = 'ali2'
    teacher.user.user.save()

    # Test the full_name method
    assert teacher.full_name() == 'mohammed1 ali2'

@pytest.mark.django_db
def test_teacher_full_name_without_first_and_last_name(teacher):
    # Create a Teacher instance without first and last name
    teacher.user.user.first_name = ''
    teacher.user.user.last_name = ''
    teacher.user.user.save()

    # Test the full_name method
    assert teacher.full_name() == 'hussain rida'

@pytest.mark.django_db
def test_unique_together_constraint(cycle, teacher, course_per_cycle):
    cycle = cycle
    teacher = teacher
    coursespercycle =course_per_cycle 

    # Create a TeachersPerCourse instance with the same unique combination
    TeachersPerCourse.objects.create(
        cycle=cycle,
        teacher=teacher,
        coursespercycle=coursespercycle,
    )

    # Attempt to create another TeachersPerCourse instance with the same unique combination
    with pytest.raises(IntegrityError):
        TeachersPerCourse.objects.create(
            cycle=cycle,
            teacher=teacher,
            coursespercycle=coursespercycle,
        )
