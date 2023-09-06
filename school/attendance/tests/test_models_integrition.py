import pytest

from datetime import datetime, timedelta
from django.utils import timezone

from django.db.utils import IntegrityError

from ..models import Attendance

'''
this section for testing attendance model
'''

@pytest.mark.django_db
def test_attendance_course_integration_error(cycle,student, sample_class):
    # Create an aware datetime for the leave time, ensuring it's after the arrive time

    timearrive = timezone.now()
    timeleave = timearrive + timezone.timedelta(minutes=40)  # Adjust the duration as needed

    # Test integration error: Attempt to create Attendance with a non-existing Course
    with pytest.raises(IntegrityError):
        Attendance.objects.create(
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=timearrive,
            timeleave=timeleave, 
        )

@pytest.mark.django_db
def test_attendance_cycle_integration_error(course,student,sample_class):
    # Test integration error: Attempt to create Attendance with a non-existing Cycle

    timearrive = timezone.now()
    timeleave = timearrive + timezone.timedelta(minutes=40)  # Adjust the duration as needed

    # Test integration error: Attempt to create Attendance with a non-existing Course
    with pytest.raises(IntegrityError):
        Attendance.objects.create(
            course=course,
            student=student,
            class_info=sample_class,
            timearrive=timearrive,
            timeleave=timeleave, 
        )

@pytest.mark.django_db
def test_attendance_student_integration_error(course,cycle,sample_class):
    # Test integration error: Attempt to create Attendance with a non-existing Student

    timearrive = timezone.now()
    timeleave = timearrive + timezone.timedelta(minutes=40)  # Adjust the duration as needed

    # Test integration error: Attempt to create Attendance with a non-existing Course
    with pytest.raises(IntegrityError):
        Attendance.objects.create(
            course=course,
            cycle=cycle,
            class_info=sample_class,
            timearrive=timearrive,
            timeleave=timeleave, 
        )

@pytest.mark.django_db
def test_attendance_class_info_integration_error(course,student,cycle):
    # Test integration error: Attempt to create Attendance with a non-existing Class

    timearrive = timezone.now()
    timeleave = timearrive + timezone.timedelta(minutes=40)  # Adjust the duration as needed
    with pytest.raises(IntegrityError):
        Attendance.objects.create(
            course=course,
            cycle=cycle,
            student=student,
            timearrive=timearrive,
            timeleave=timeleave, 
        )
