import pytest

from ..course.models import Course, CoursesPerCycle
@pytest.fixture
def course(category):
    course =  Course.objects.create(
        code="CS101",
        name="Introduction to Computer Science",
        category=category,
        description="This is a sample course description.",
    )
    return course

@pytest.fixture
def course_per_cycle(course, cycle):
    cpc =  CoursesPerCycle.objects.create(
        course=course,
        cycle=cycle,
        coursestartdate="2023-01-01",
        courseenddate="2023-12-31",
    )
    return cpc
