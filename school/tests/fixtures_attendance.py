from django.utils import timezone
import pytest

from ..attendance.models import Attendance

@pytest.fixture
def attendance(course, cycle, sample_class, student):

    # Create an aware datetime for the arrive time
    timearrive = timezone.now()

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timeleave = timearrive + timezone.timedelta(minutes=40)  # Adjust the duration as needed

    attendance = Attendance.objects.create(
        course=course,
        cycle=cycle,
        class_info = sample_class,
        timearrive=timearrive,
        timeleave=timeleave, 
        student=student,

    )
    return attendance
