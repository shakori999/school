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

@pytest.mark.django_db
def test_teacher_str_method(teacher):

    teacher.user.user.first_name = 'jasim'
    teacher.user.user.last_name = 'abbas'
    teacher.user.user.save()

    # Test the __str__ method
    assert str(teacher) == 'jasim abbas'

