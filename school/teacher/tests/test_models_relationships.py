import pytest
from ..models import Teacher,TeachersPerCourse

'''
this section for testing teacher model
'''

@pytest.mark.django_db
def test_teachers_relationship(teacher, person_teacher):
    # Create a teacher instance
    teacher = teacher
    # Retrieve the created Teachers instance from the database
    tpc_from_db = Teacher.objects.get(id=teacher.id)

    # Perform assertions to check the relationships
    assert tpc_from_db.user == person_teacher 


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
