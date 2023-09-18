import pytest 
from datetime import time

from django.utils import timezone
from django.db import IntegrityError, transaction

from ..models import Class
from ...attendance.models import Attendance
from ...student.models import Student

'''
this section for testing class model
'''
@pytest.mark.django_db
def test_unique_class_title(course, cycle, course_per_cycle):
    # Test invalid data: Duplicate class title
    timenow = timezone.now().date()
    valid_class = Class(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate=timenow,
        starttime=time(9, 0, 0),
        endtime=time(11, 0, 0),
    )
    valid_class.save()

    with pytest.raises(IntegrityError) as e:
        with transaction.atomic():
            invalid_class = Class(
                course=course,
                cycle=cycle,
                coursespercycle=course_per_cycle,
                classno=2,
                classtitle="Sample Class",
                classdate=timenow,
                starttime=time(10, 0, 0),
                endtime=time(12, 0, 0),
            )
            invalid_class.save()

    # Ensure that the IntegrityError is raised
    assert isinstance(e.value, IntegrityError)

@pytest.mark.django_db
def test_course_foreign_key_integrity():
    # Test that the foreign key relationship with the Course model is enforced properly
    with pytest.raises(IntegrityError):
        Class.objects.create(
            classno=1,
            classtitle="Test Class",
            classdate=timezone.now().date(),
            starttime=timezone.now().time(),
            endtime=(timezone.now() + timezone.timedelta(hours=1)).time(),
            course=None  # Use an invalid course object
        )

@pytest.mark.django_db
def test_cycle_foreign_key_integrity():
    # Test that the foreign key relationship with the Cycle model is enforced properly
    with pytest.raises(IntegrityError):
        Class.objects.create(
            classno=2,
            classtitle="Test Class",
            classdate=timezone.now().date(),
            starttime=timezone.now().time(),
            endtime=(timezone.now() + timezone.timedelta(hours=1)).time(),
            cycle=None  # Use an invalid cycle object
        )

@pytest.mark.django_db
def test_courses_per_cycle_foreign_key_integrity():
    # Test that the foreign key relationship with the CoursesPerCycle model is enforced properly
    with pytest.raises(IntegrityError):
        Class.objects.create(
            classno=3,
            classtitle="Test Class",
            classdate=timezone.now().date(),
            starttime=timezone.now().time(),
            endtime=(timezone.now() + timezone.timedelta(hours=1)).time(),
            coursespercycle=None  # Use an invalid courses_per_cycle object
        )

@pytest.mark.django_db
def test_students_many_to_many_relationship(student,course, course_per_cycle, cycle):
    # Test that the many-to-many relationship with the Student model through the Attendance model is working as expected
    class_obj = Class.objects.create(
        classno=4,
        classtitle="Test Class",
        classdate=timezone.now().date(),
        starttime=timezone.now().time(),
        endtime=(timezone.now() + timezone.timedelta(hours=1)).time(),
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
    )
    # Create an attendance record to associate the student with the class
    Attendance.objects.create(
            class_info=class_obj,
            student=student,
            timearrive=timezone.now().time(),
            timeleave=(timezone.now() + timezone.timedelta(hours=1)).time(),
            course=course,
            cycle=cycle,
            )
    assert class_obj.students.count() == 1  # Check if the student is associated with the class
