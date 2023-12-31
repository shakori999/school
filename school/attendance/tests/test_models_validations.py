import pytest
from datetime import timedelta,datetime
from django.core.exceptions import ValidationError
from django.utils import timezone


from ..models import Attendance

'''
this section for testing attendance model
'''
@pytest.mark.django_db
def test_attendance_timearrive_before_timeleave(student, course, cycle, sample_class):

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timearrive = timezone.now().time()

    timearrive_datetime = datetime.combine(datetime.today(), timearrive)
    timeleave = timearrive_datetime - timezone.timedelta(minutes=40)  # Adjust the duration as needed
    newleave = timeleave.time()

    # Attempt to create an Attendance instance with arrival time after leave time
    with pytest.raises(ValidationError) as e:
        invalid_attendance = Attendance.objects.create(
            course=course,
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=timearrive ,  # Arrival time after leave time
            timeleave=newleave,  # Leave time
        )
        invalid_attendance.full_clean()

    # Check that the expected validation error message is raised
    assert "Arrival time must be before leave time" in str(e.value)

@pytest.mark.django_db
def test_attendance_timearrive_is_none(course, cycle, student, sample_class):
    # Test invalid data: Arrival time is None
    with pytest.raises(ValidationError) as e:
        invalid_attendance = Attendance(
            course=course,
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=None,
            timeleave=timezone.now(),
        )
        invalid_attendance.full_clean()
    assert "This field cannot be null." in str(e.value)

@pytest.mark.django_db
def test_attendance_timeleave_is_none(course, cycle, student, sample_class):
    # Test invalid data: Leave time is None
    with pytest.raises(ValidationError) as e:
        invalid_attendance = Attendance(
            course=course,
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=timezone.now(),
            timeleave=None,
        )
        invalid_attendance.full_clean()
    assert "This field cannot be null." in str(e.value)

@pytest.mark.django_db
def test_attendance_timearrive_and_timeleave_are_none(course, cycle, student, sample_class):
    # Test invalid data: Arrival and leave times are None
    with pytest.raises(ValidationError) as e:
        invalid_attendance = Attendance(
            course=course,
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=None,
            timeleave=None,
        )
        invalid_attendance.full_clean()
    assert "This field cannot be null." in str(e.value)

@pytest.mark.django_db
def test_attendance_timearrive_in_future(course, cycle, student, sample_class):

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timearrive = timezone.now().time()

    timearrive_datetime = datetime.combine(datetime.today(),timearrive)
    timeleave = timearrive_datetime - timezone.timedelta(minutes=40)  # Adjust the duration as needed
    newleave = timeleave.time()

    # Test invalid data: Arrival time in the future
    with pytest.raises(ValidationError) as e:
        invalid_attendance = Attendance.objects.create(
            course=course,
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=timearrive,
            timeleave=newleave,
        )
        invalid_attendance.full_clean()
    assert "Arrival time must be before leave time" in str(e.value)

@pytest.mark.django_db
def test_attendance_timeleave_in_past(course, cycle, student, sample_class):
    future = timezone.now() - timedelta(days=1)

    # Test invalid data: Leave time in the future
    with pytest.raises(ValidationError) as e:
        invalid_attendance = Attendance.objects.create(
            course=course,
            cycle=cycle,
            student=student,
            class_info=sample_class,
            timearrive=timezone.now(),
            timeleave=future,
        )
        invalid_attendance.full_clean()
    assert "Arrival time must be before leave time" in str(e.value)
