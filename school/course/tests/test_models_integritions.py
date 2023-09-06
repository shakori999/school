import pytest

from django.db import IntegrityError

from ..models import Course, CoursesPerCycle

'''
this section for testing coruse model
'''
@pytest.mark.django_db
def test_course_cycles_through(cycle):
    # Test that a Course instance is associated with cycles correctly through the CoursesPerCycle model
    course = Course(code="COURSE101", name="Sample Course", description="A description.")
    course.save()
    with pytest.raises(IntegrityError) as e:
        course.cycles.add(cycle)
        course.save()

    assert isinstance(e.value, IntegrityError)

'''
this section for testing corusepercycle model
'''

@pytest.mark.django_db
def test_courses_per_cycle_start_date_before_end_date(course, cycle):
    # Test invalid data: Course start date after course end date
    with pytest.raises(IntegrityError):
        CoursesPerCycle.objects.create(
            course=course,
            cycle=cycle,
            coursestartdate="2023-09-01",
            courseenddate="2023-08-31",  # Course start date later than end date
        )
