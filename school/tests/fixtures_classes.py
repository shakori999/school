import pytest

from django.utils import timezone

from ..classes.models import Class 

@pytest.fixture
def sample_class(course, cycle, course_per_cycle):
    timenow = timezone.now().date()
    class_instance = Class.objects.create(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate=timenow,
        starttime="09:00:00",
        endtime="11:00:00",
    )
    return class_instance
