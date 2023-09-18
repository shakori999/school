import pytest

from datetime import time,datetime ,timedelta

from django.utils import timezone

from ..classes.models import Class 

@pytest.fixture
def sample_class(course, cycle, course_per_cycle):

    # Create an aware datetime for the leave time, ensuring it's after the arrive time
    timearrive = timezone.now().time()
    timearrive_str = timearrive.strftime('%H:%M:%S')

    timeleave_datetime = datetime.combine(datetime.today(), timearrive) + timedelta(minutes=40)
    timeleave_str = timeleave_datetime.strftime('%H:%M:%S')

    timenow = timezone.now().date()

    class_instance = Class.objects.create(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate=timenow,
        starttime=timearrive_str,
        endtime=timeleave_str,
    )
    return class_instance
