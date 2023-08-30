import pytest
from ..models import Enrollment, Student

'''
this section for testing student model
'''
@pytest.mark.django_db
def test_student_relationship(student, person_student, course_per_cycle, sample_class):
    # Create a student instance
    student = student
    # Retrieve the created Student instance from the database
    stu_from_db = Student.objects.get(id=student.id)

    # Retrieve the courses related to the student
    related_courses = stu_from_db.courses_per_cycle.all()
    related_classes = stu_from_db.classes.all()
    print(related_classes)

    # Perform assertions to check the relationships
    assert stu_from_db.user == person_student 
    assert course_per_cycle in related_courses

'''
this section for testing enrollment model
'''

@pytest.mark.django_db
def test_enrollment_relationship(student, enrollment, course_per_cycle):
    # Create an enrollment instance
    en = enrollment
    # Retrieve the created Enrollment instance from the database
    en_from_db = Enrollment.objects.get(id=en.id)

    # Perform assertions to check the relationships
    assert en_from_db.student == student 
    assert en_from_db.course_per_cycle == course_per_cycle 
