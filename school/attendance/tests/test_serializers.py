import pytest
from django.utils import timezone

from ..serializers import AttendanceSerializer

@pytest.mark.django_db
def test_arrive_time_in_future_serializer(course, cycle, sample_class, student):
    # Create data for the serializer
    data = {
        "course": course.id,  # Replace with the appropriate course ID
        "cycle": cycle.id,   # Replace with the appropriate cycle ID
        "student": student.id, # Replace with the appropriate student ID
        "class_info": sample_class.id,  # Replace with the appropriate class ID
        "timearrive": timezone.now() + timezone.timedelta(hours=1),  # Set arrive time in the future
        "timeleave": timezone.now(),  # Set leave time to the current time
    }

    # Create an instance of the serializer with the data
    serializer = AttendanceSerializer(data=data)

    # Validate the serializer data
    assert not serializer.is_valid()
    assert "Arrival time cannot be in the future" in str(serializer.errors)

@pytest.mark.django_db
def test_arrive_time_after_leave_time(course, cycle, sample_class, student):
    data = {
        "course": course.id,  # Replace with the appropriate course ID
        "cycle": cycle.id,   # Replace with the appropriate cycle ID
        "student": student.id, # Replace with the appropriate student ID
        "class_info": sample_class.id,  # Replace with the appropriate class ID
        "timearrive": timezone.now() ,  # Set arrive time in the future
        "timeleave": timezone.now() - timezone.timedelta(hours=1),  # Set leave time to the current time
    }
    serializer = AttendanceSerializer(data=data)

    # Validate the serializer data
    assert not serializer.is_valid()

    assert "Arrival time must be before leave time" in str(serializer.errors)

@pytest.mark.django_db
def test_create_valid_attendance_record(course, cycle, sample_class, student):
    data = {
        "course": course.id,  # Replace with the appropriate course ID
        "cycle": cycle.id,   # Replace with the appropriate cycle ID
        "student": student.id, # Replace with the appropriate student ID
        "class_info": sample_class.id,  # Replace with the appropriate class ID
        "timearrive": timezone.now() ,  # Set arrive time in the future
        "timeleave": timezone.now() + timezone.timedelta(hours=1),  # Set leave time to the current time
    }
    serializer = AttendanceSerializer(data=data)

    assert serializer.is_valid()

    # Create an attendance record by saving the serializer
    attendance = serializer.save()

    # Perform assertions

    # Access fields from validated_data
    timearrive = serializer.validated_data["timearrive"]
    timeleave = serializer.validated_data["timeleave"]

    assert attendance.timearrive <= attendance.timeleave
    assert attendance.timearrive <= timezone.now()
    assert attendance.id is not None  # Check that an ID has been assigned to the attendance record
    assert timearrive <= timeleave
    assert timearrive <= timezone.now()
