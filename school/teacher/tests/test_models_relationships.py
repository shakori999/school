import pytest
from ..models import Person, Teacher,TeachersPerCourse

'''
this section for testing teacher model
'''

@pytest.mark.django_db
def test_teachers_relationship(teacher):
    # Create a teacher instance
    teacher = teacher
    # Retrieve the created Teachers instance from the database
    tpc_from_db = Teacher.objects.get(id=teacher.id)
    per_from_db = Person.objects.get(id=teacher.user.id)

    # Perform assertions to check the relationships
    assert tpc_from_db.user == per_from_db 


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
