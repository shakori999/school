import pytest

from ..classes.models import Class 

@pytest.fixture
def sample_class(course, cycle, course_per_cycle):
    class_instance = Class.objects.create(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate="2023-09-01",
        starttime="09:00:00",
        endtime="11:00:00",
    )
    return class_instance
