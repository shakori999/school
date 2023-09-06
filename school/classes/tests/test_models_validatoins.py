import pytest
from datetime import time

from django.utils import timezone
from django.db import transaction
from django.core.exceptions import ValidationError

from ..models import Class


@pytest.mark.django_db
def test_classno_positive(course,cycle,course_per_cycle):
    # Test valid data: Positive class number
    timenow = timezone.now().date()
    valid_class = Class(
        course=course,
        cycle=cycle,
        coursespercycle=course_per_cycle,
        classno=1,
        classtitle="Sample Class",
        classdate=timenow,
        starttime=time(9, 0, 0),
        endtime=time(11, 0, 0),
    )
    valid_class.full_clean()


@pytest.mark.django_db
def test_classno_negative(course, cycle, course_per_cycle):
    # Test invalid data: Negative class number
    timenow = timezone.now().date()
    with pytest.raises(ValidationError) as e:
        with transaction.atomic():  # Save outside of the transaction
            invalid_class = Class(
                course=course,
                cycle=cycle,
                coursespercycle=course_per_cycle,
                classno=-1,
                classtitle="Sample Class",
                classdate=timenow,
                starttime=time(9, 0, 0),
                endtime=time(11, 0, 0),
            )
            invalid_class.save()
        assert "Class number must be greater than or equal to 0" in str(e.value)

    # Ensure that the validation error is raised
    assert "Class number must be greater than or equal to 0" in str(e.value)

@pytest.mark.django_db
def test_starttime_after_endtime(course, cycle, course_per_cycle):
    # Test invalid data: Start time after end time
    timenow = timezone.now().date()
    with pytest.raises(ValidationError) as e:
        with transaction.atomic():
            invalid_class = Class(
                course=course,
                cycle=cycle,
                coursespercycle=course_per_cycle,
                classno=1,
                classtitle="Sample Class",
                classdate=timenow,
                starttime=time(12, 0, 0),
                endtime=time(11, 0, 0),
            )
            invalid_class.save()
        assert "Start time must be before end time" in str(e.value)

    # Ensure that the validation error is raised
    assert "Start time must be before end time" in str(e.value)


@pytest.mark.django_db
def test_class_date_in_past(course, cycle, course_per_cycle):
    # Test invalid data: Class date in the past

    timenow = timezone.now().date()
    with pytest.raises(ValidationError) as e:
        with transaction.atomic():
            invalid_class = Class(
                course=course,
                cycle=cycle,
                coursespercycle=course_per_cycle,
                classno=1,
                classtitle="Sample Class",
                classdate=timenow - timezone.timedelta(days=1),
                starttime=time(9, 0, 0),
                endtime=time(11, 0, 0),
            )
            invalid_class.save()

    # Ensure that the validation error message is as expected
    assert "Class date cannot be in the past" in str(e.value)
