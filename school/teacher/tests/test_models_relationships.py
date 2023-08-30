import pytest

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

"""
this section for testing teacherpercourse model
"""

@pytest.mark.django_db
def test_teachers_per_course_relationship(teachers_per_course, cycle, teacher, course_per_cycle):
    # Create a TeachersPerCourse instance
    tpc = teachers_per_course
    # Retrieve the created TeachersPerCourse instance from the database
    tpc_from_db = TeachersPerCourse.objects.get(id=tpc.id)

    # Perform assertions to check the relationships
    assert tpc_from_db.cycle == cycle
    assert tpc_from_db.teacher == teacher
    assert tpc_from_db.coursespercycle ==course_per_cycle 
