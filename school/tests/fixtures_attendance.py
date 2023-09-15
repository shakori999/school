import pytest

from django.utils import timezone

from ..attendance.models import Attendance
from ..attendance.serializers import AttendanceSerializer

from rest_framework.test import APIClient

@pytest.fixture
def attendance(course, cycle, sample_class, student):

    # Create an aware datetime for the arrive time
    timearrive = timezone.now().time()

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timeleave = timearrive   # Adjust the duration as needed

    attendance = Attendance.objects.create(
        course=course,
        cycle=cycle,
        class_info = sample_class,
        timearrive=timearrive,
        timeleave=timeleave, 
        student=student,

    )
    return attendance

@pytest.fixture
def serializer():
    return AttendanceSerializer()


@pytest.fixture
def api_client():
    return APIClient()
